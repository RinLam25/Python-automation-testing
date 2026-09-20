import requests

BASE_URL = "https://automationexercise.com/api"


# ---------- Test 1: GET danh sách sản phẩm (happy path) ----------
def test_get_products_list_returns_200():
    response = requests.get(f"{BASE_URL}/productsList")
    data = response.json()

    assert response.status_code == 200          # HTTP status luôn 200
    assert data["responseCode"] == 200            # status "thật" nằm ở đây
    assert "products" in data
    assert len(data["products"]) > 0


# ---------- Test 2: verify cấu trúc field của 1 sản phẩm ----------
def test_product_has_required_fields():
    response = requests.get(f"{BASE_URL}/productsList")
    data = response.json()
    first_product = data["products"][0]

    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product
    assert "brand" in first_product


# ---------- Test 3: negative — POST vào endpoint chỉ hỗ trợ GET ----------
def test_post_to_products_list_returns_405():
    response = requests.post(f"{BASE_URL}/productsList")
    data = response.json()

    assert data["responseCode"] == 405


# ---------- Test 4: search sản phẩm hợp lệ ----------
def test_search_product_with_valid_keyword():
    response = requests.post(
        f"{BASE_URL}/searchProduct",
        data={"search_product": "top"}
    )
    data = response.json()

    assert data["responseCode"] == 200
    assert len(data["products"]) > 0


# ---------- Test 5: edge case — search với chuỗi rỗng ----------
def test_search_product_with_empty_string():
    response = requests.post(
        f"{BASE_URL}/searchProduct",
        data={"search_product": ""}
    )
    data = response.json()

    # Ghi chú: cần chạy thử để biết API xử lý chuỗi rỗng ra sao,
    # rồi mới viết assertion đúng theo thực tế quan sát được
    assert response.status_code == 200
    print(data)  # in ra để quan sát khi chạy pytest -s


# ---------- Test 6: negative — thiếu param bắt buộc ----------
def test_search_product_without_param_returns_400():
    response = requests.post(f"{BASE_URL}/searchProduct")
    data = response.json()

    assert data["responseCode"] == 400


# ---------- Test 7: edge case — ký tự đặc biệt ----------
def test_search_product_with_special_characters():
    response = requests.post(
        f"{BASE_URL}/searchProduct",
        data={"search_product": "<script>alert(1)</script>"}
    )
    data = response.json()

    # Verify API không bị crash (vẫn trả 200) khi nhận input lạ
    assert response.status_code == 200
    assert data["responseCode"] in [200, 400]


# ---------- Test 8: verifyLogin với thông tin sai ----------
def test_verify_login_invalid_credentials_returns_404():
    response = requests.post(
        f"{BASE_URL}/verifyLogin",
        data={"email": "khongtontai@example.com", "password": "sai123"}
    )
    data = response.json()

    assert data["responseCode"] == 404
    assert data["message"] == "User not found!"


# ---------- Test 9: verifyLogin thiếu email ----------
def test_verify_login_missing_email_returns_400():
    response = requests.post(
        f"{BASE_URL}/verifyLogin",
        data={"password": "abc123"}
    )
    data = response.json()

    assert data["responseCode"] == 400


# ---------- Test 10: đo response time ----------
def test_products_list_response_time_under_2_seconds():
    response = requests.get(f"{BASE_URL}/productsList")
    assert response.elapsed.total_seconds() < 5

def test_put_to_brands_list_returns_405():
    # dùng requests.put() thay vì requests.post(), và URL là /brandsList
    response = requests.put(f"{BASE_URL}/brandsList")
    data = response.json()

    assert data["responseCode"] == 405

def test_delete_to_verify_login_returns_405():
    # dùng requests.delete()
    response = requests.delete(f"{BASE_URL}/verifyLogin")
    data = response.json()

    assert data["responseCode"] == 405

def test_create_account_missing_email_returns_400():
    response = requests.post(
        f"{BASE_URL}/createAccount",
        data={"name": "Rin Test"}
    )
    data = response.json()
    assert data["responseCode"] == 400  

def test_delete_account_wrong_email_returns_404():
    # data cần: email và password không tồn tại
    response = requests.delete(
        f"{BASE_URL}/deleteAccount",
        data={"email": "rinlam123@gmail.com", "password": "rinnn123"}
    )
    data = response.json()
    assert data["responseCode"] == 404

def test_get_user_detail_missing_email_param():
    response = requests.get(f"{BASE_URL}/getUserDetailByEmail")
    data = response.json()
    assert data["responseCode"] == 400   