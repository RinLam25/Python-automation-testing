import requests


def get_products_safely():
    """Hàm giả lập logic xử lý: gọi API, nếu lỗi thì trả về danh sách rỗng thay vì crash"""
    try:
        response = requests.get("https://automationexercise.com/api/productsList")
        if response.status_code == 200:
            return response.json().get("products", [])
        return []
    except requests.exceptions.RequestException:
        return []


def test_get_products_safely_handles_server_error(mocker):
    # Giả lập requests.get() trả về response lỗi 500, không gọi mạng thật
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mocker.patch("requests.get", return_value=mock_response)

    result = get_products_safely()

    # Verify: khi server lỗi, hàm phải trả về list rỗng, không được crash
    assert result == []


def test_get_products_safely_handles_success(mocker):
    # Giả lập response thành công với data tự đặt ra
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "products": [{"id": 1, "name": "Sản phẩm giả lập"}]
    }
    mocker.patch("requests.get", return_value=mock_response)

    result = get_products_safely()

    assert len(result) == 1
    assert result[0]["name"] == "Sản phẩm giả lập"


def test_get_products_safely_handles_network_error(mocker):
    # Giả lập trường hợp mất mạng hoàn toàn
    mocker.patch("requests.get", side_effect=requests.exceptions.ConnectionError)

    result = get_products_safely()

    assert result == []

def check_inventory():
    """Hàm giả lập: gọi API kiểm tra tồn kho, trả về True nếu còn hàng, False nếu hết"""
    try:
        response = requests.get("https://vidu.com/api/tonkho")
        if response.status_code == 200:
            data = response.json()
            return data["so_luong"] > 0
        return False
    except requests.exceptions.RequestException:
        return False

def test_kiem_tra_ton_kho_con_hang(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"so_luong": 10}
    mocker.patch("requests.get", return_value = mock_response )
    result = check_inventory()
    assert result == True

def test_kiem_tra_ton_kho_het_hang(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"so_luong": 0}
    mocker.patch("requests.get", return_value = mock_response )
    result = check_inventory()
    assert result == False

def test_mat_mang(mocker):
    mocker.patch("requests.get", side_effect = requests.exceptions.ConnectionError)
    result = check_inventory()
    assert result == False