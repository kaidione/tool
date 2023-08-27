import os

import yaml


# https://verytoolz.com/yaml-formatter.html

def readYaml(path):
    with open(path, "+r", encoding="utf-8") as file:
        data = yaml.load(stream=file, Loader=yaml.FullLoader)
        return data


def get_yaml(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as fp:
        f = fp.read()  # 读出来是字符串
        print(type(f))
    d = yaml.load(f)  # 转列表
    print("读取到yaml文件数据")
    print(d)
    print(type(d))
    return d


'''
增加数据
'''


def add_dict(a, b, yamlPath):
    data = {a: b}
    file = open(yamlPath, 'a', encoding='utf-8')
    yaml.dump(data, file)
    file.close()


# add_dict('a','666')
# print(get_dict())
'''
删除操作
'''


def delete_data(key):
    d = {}
    with open('in.yaml', 'r+') as f:
        dict_temp = yaml.load(f, Loader=yaml.FullLoader)
        print(dict_temp)
        print(type(dict_temp))
        dict_temp.pop(key)
    with open('in.yaml', 'w') as f:
        yaml.dump(dict_temp, f)  # 将Python中的字典或者列表转化为yaml格式的数据
        f.close()
        return d


# delete_data('b')
# print(get_dict())


'''
修改操作
'''


def change_data(key, data):
    with open('in.yaml') as f:
        dict_temp = yaml.load(f, Loader=yaml.FullLoader)
        dict_temp[key] = data
    with open('in.yaml', 'w') as f:
        yaml.dump(dict_temp, f)  # 将Python中的字典或者列表转化为yaml格式的数据
        f.close()


# change_data('b', 'D')
# print(get_dict())

import json
import jsonpath

import chardet
import codecs


def convert_file_to_utf8(filename):
    # !!! does not backup the origin file
    content = codecs.open(filename, 'r').read()
    source_encoding = chardet.detect(bytes(content))
    if source_encoding is None:
        print("encoding is None: %s" % filename)
        return
    print("[%s]--->[%s]: %s" % (filename, source_encoding, 'utf-8'))
    if source_encoding != 'utf-8':
        content = content.decode(source_encoding, 'ignore').encode("utf-8")
        codecs.open(filename, 'w', encoding='utf-8').write(content)


def find_max_layer(d):
    return max(find_max_layer(v) if isinstance(v, dict) else 0 for v in d.values()) + 1


# p = maxDepth(d)
# print('字典的最大深度是:　', p)　

def Json_to_Python(path_json):
    # with open(path_json) as f:
    #     content = f.read()
    #     if content.startswith(u'\eff'):
    #         content = content.encode('utf8')[3:].decode('utf8')
    # convert_file_to_utf8(path_json)
    # 以上解决编码含有dom的问题
    All_value = []
    obj = json.load(open(path_json, 'r', encoding='utf-8-sig', errors='ignore'), strict=False)  # 注意，这里是文件的形式，不能直接放一个文件名的字符串
    # obj = json.load(open(path_json, 'r', encoding="'utf8'[3:].decode('utf8')"))  # 注意，这里是文件的形式，不能直接放一个文件名的字符串
    # obj = json.load(open(path_json, 'r', encoding='gb18030', errors='ignore'))
    # print(find_max_layer(obj))
    deep = find_max_layer(obj)
    # print(deep)
    if deep == 1:
        for k in obj:
            # print(obj[k])
            list_value = jsonpath.jsonpath(obj, '$..' + k)
            All_value.append(list_value)
    elif deep == 2:
        for k in obj:
            # print(obj[k])
            for k2 in obj[k]:
                list_value = jsonpath.jsonpath(obj, '$..' + k2)
                All_value.append(list_value)

    elif deep == 3:
        for k in obj:
            # print(obj[k])
            for k2 in obj[k]:
                for k3 in obj[k][k2]:
                    # print(obj[k][k2][k3])
                    list_value = jsonpath.jsonpath(obj, '$..' + k3)
                    All_value.append(list_value)
    # print(All_value)
    return All_value
    # print(obj.values())
    # print(type(obj))
    # print(obj[2])

    # if obj[key]
    # city_list = jsonpath.jsonpath(obj, '$..regionName')  # 文件对象   jsonpath语法
    # list_value = jsonpath.jsonpath(obj, '$..')  # 文件对象   jsonpath语法
    # list_value.count()
    # return list_value
    # print(city_list)


def Txt_to_Json(path_txt):
    with open(path_txt, 'r', encoding='utf-8')as f:  # 打开txt文件
        for line in f:
            d = {'content': line.rstrip('\n')}
            with open('file.json', 'a', encoding='utf-8')as file:  # 创建一个json文件，mode设置为'a'
                json.dump(d, file,
                          ensure_ascii=False)  # 将字典d写入json文件中，并设置ensure_ascii = False,主要是因为汉字是ascii字符码,
                # 若不指定该参数，那么文字格式就会是ascii码
                file.write('\n')


# if __name__ == '__main__':
#     rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     print(rootPath)
#     # path = os.path.join(rootPath, "data\\power\\AR")
#     path = os.path.join(rootPath, "data\\power\\AR\\") + os.listdir(os.path.join(rootPath, "data\\power\\AR"))[0]
#     print(path)
#     # path = os.path.join(rootPath, "config/config.yaml")
#     with open(path, 'rb') as f:
#         text = f.read()
#
#     chardet.detect(text)
#     print(chardet.detect(text))
#     print(Json_to_Python(path))
    # print(readYaml(path))
