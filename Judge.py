"""
!/usr/bin/python11
-*- coding: utf-8 -*-            
@Author : xuyuhao
@Time : 2023/12/29 22:30
@FileName: Judge.py
"""
from PickUpInformation import *
from Template import Template
from Tip import Tip


template = Template()


# 判断是否存在文件
def is_data_json_exist(file_path, json_template):
    try:
        read_json(file_path)
        return True
    except FileNotFoundError:
        tip = Tip("数据文件不存在，正在创建...")
        tip.show()
        write_json(file_path, json_template)
        return False


# 判断文件中的字段是否齐全
def check_fields_in_json(file_path, fields, json_template):
    json_data = read_json(file_path)
    try:
        for field in fields:
            if field not in json_data:
                tip = Tip("数据文件错误，正在修理...")
                tip.show()
                write_json(file_path, json_template)
                return False
        return True
    except:
        tip = Tip("数据文件错误，正在修理...")
        tip.show()
        return False


# 检测json文件特定字段是否为空
def check_fields_empty(file_path, fields):
    json_data = read_json(file_path)
    for field in fields:
        if json_data[field] == "":
            return False
    return True


# 等待json文件更新
def wait_json_update(file_path, fields):
    while True:
        if check_fields_empty(file_path, fields):
            write_time(file_path)
            tip = Tip("Ucopy启动成功")
            tip.show()
            break
        tip = Tip("数据文件未填写完整，为保证安全，请重新填写...")
        tip.show()
        time.sleep(2.9)


def self_examination(file_path, fields, json_template):
    is_data_json_exist(file_path, json_template)
    check_fields_in_json(file_path, fields, json_template)
    wait_json_update(file_path,  fields)


def judging_files(file_path):
    traverse(file_path)
    data = read_json(template.json_path)
    is_copy = []
    for i in lst:
        md5v = create_md5(i)
        is_have = False
        for j in data["md5"]:
            if md5v == j:
                is_copy.append(0)
                is_have = True
                break
        if not is_have:
            data["md5"].append(md5v)
            is_copy.append(i)
    write_json(template.json_path, data)
    return is_copy
