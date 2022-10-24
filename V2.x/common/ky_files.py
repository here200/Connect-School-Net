# 将文件里的数据转化为python中字典类型的数据
def file2dict(file_path, container, separator):
    with open(file_path, "r", encoding="UTF-8") as f:
        line = f.readline()
        while line:
            # 提取键值对
            pair = line.strip().split(separator)
            if len(pair) == 1:
                container[pair[0]] = ""
            else:
                container[pair[0]] = pair[1].lstrip()
            line = f.readline()


# 读取文件中的字符串数据
def file2string(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        data = f.read()
    return data
