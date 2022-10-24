from common import ky_files, ky_requests, ky_res


def get_query_string(url, data):
    ky_res.cache = ky_requests.decode_response(ky_requests.get(url=url))
    data["queryString"] = ky_res.get_one_data("<script>top.self.location.href.*[?](.*)'</script>")


def start():
    # url, headers and label-data
    headers = {}
    data = {}
    try:
        url = ky_files.file2string("./data/url.txt")
        ky_files.file2dict("./data/header.txt", headers, ":")
        ky_files.file2dict("./data/label-data.txt", data, ":")
    except Exception:
        raise Exception("文件读写错误，请检查文件里数据是否正确")

    # get queryString
    query_string_url = "http://" + data["queryString"]
    try:
        get_query_string(url=query_string_url, data=data)
    except Exception:
        raise Exception("你已经连接到校园网了，祝你玩的开心。")

    # send a post request, and parse the response
    try:
        response = ky_requests.post(url=url, headers=headers, data=data)
        print(ky_requests.decode_response(response))
    except Exception:
        raise Exception("发送请求失败，请检查url是否正确，或者是否已经到连接正确的网络")


if __name__ == '__main__':
    start()
