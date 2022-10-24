import requests


def post(headers, url, data):
    return requests.post(headers=headers, url=url, data=data, timeout=10)


def decode_response(response):
    return response.content.decode()
