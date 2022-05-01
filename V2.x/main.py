import requests
import re


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


class Connect_School_Net(object):
    def __init__(self):
        # 请求url
        self.url = ''
        # 请求头
        self.header = {}
        # 表单
        self.data = {}
        # 临时发送请求用的请求头
        self.tmpHeader = {}

    # 获取数据，如果获取失败，直接退出程序
    def get_data(self, url):
        try:
            response = requests.get(url=url, headers=self.tmpHeader, timeout=10)
            return response.content
        except:
            print("发送请求失败，请检查是否已经到连接正确的网络")
            exit()

    # 获取查询字符串
    def getQueryString(self):
        # 1. 构造发送url
        queryString_url = 'http://' + self.data['queryString']
        # 发送请求，获取响应
        response = self.get_data(queryString_url)
        # 2. 提取查询字符串
        # 如果出现异常，则说明用户已经连接到校园网了
        tmpStr = ''
        try:
            tmpStr = response.decode()
        except:
            print("You have been online.")
            exit()
        pattern = re.compile("<script>top.self.location.href.*[?](.*)'</script>")
        # 3. 将查询字符串保存到data中
        self.data['queryString'] = pattern.match(tmpStr)[1]

    def connect(self):
        try:
            response = requests.post(url=self.url, data=self.data, headers=self.header, timeout=10)
            # 打印响应中的数据
            print(response.content.decode())
        except:
            print('请检查url是否正确')
            exit()

    def start(self):
        # url, headers and label-data
        try:
            with open("./data/url.txt", "r") as f:
                self.url = f.read()
            fileToDict("./data/header.txt", self.header, ":")
            fileToDict("./data/label-data.txt", self.data, ":")
        except:
            print('文件读写错误，请检查文件里数据是否正确')
            exit()
        # 创建临时请求头
        self.tmpHeader = {
            'User-Agent': self.header['User-Agent']
        }
        # 获取查询字符串
        self.getQueryString()
        # 连接校园网
        self.connect()

if __name__ == '__main__':
    t = Connect_School_Net()
    t.start()
