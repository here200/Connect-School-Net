import requests

_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
}


def get(url, params=None, headers=None):
    if headers is None:
        headers = _headers
    return requests.get(headers=headers, url=url, params=params, timeout=10)


def post(url, data=None, headers=None):
    if headers is None:
        headers = _headers
    return requests.post(headers=headers, url=url, data=data, timeout=10)


def decode_response(response):
    return response.content.decode()
