import pytest

DOMAIN_QUANG_CAO = [
    "doubleclick.net",
    "googlesyndication.com",
    "google.com/pagead",
    "tiktok.com",
    "amazon-adsystem.com",
    "adservice.google.com",
]

@pytest.fixture(autouse=True)
def chan_quang_cao(page):
    def xu_ly_request(route):
        url = route.request.url
        if any(domain in url for domain in DOMAIN_QUANG_CAO):
            route.abort()      # chặn, không cho request này tải
        else:
            route.continue_()  # cho phép request bình thường tiếp tục

    page.route("**/*", xu_ly_request)
    yield