import requests

# 将文件里的数据转化为python中字典类型的数据
def fileToDict(fileName, container, separator):
    with open(fileName, "r") as f:
        line = f.readline()
        while line:
            str = line.strip().split(separator)
            if len(str) == 1:
                container[str[0]] = ""
            else:
                container[str[0]] = str[1].lstrip()
            line = f.readline()

# main_process
def start():
    # url, headers and label-data
    url = ''
    header = {}
    data = {}
    try:
        with open("./data/url.txt", "r") as f:
            url = f.read()
        fileToDict("./data/header.txt", header, ":")
        fileToDict("./data/label-data.txt", data, ":")
    except:
        print('文件读写错误，请检查文件里数据是否正确')
        exit()

    # 发送请求，并获取响应
    try:
        response = requests.post(url=url, data=data, headers=header, timeout=10)
        # 打印响应中的数据
        print(response.content.decode())
    except:
        print("发送请求失败，请检查url是否正确，或者是否已经到连接正确的网络")
        exit()


if __name__ == '__main__':
    start()
