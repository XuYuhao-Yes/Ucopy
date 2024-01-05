"""
!/usr/bin/python11
-*- coding: utf-8 -*-            
@Author : xuyuhao
@Time : 2023/12/29 22:09
@FileName: PickUpInformation.py
"""
import shutil
from hashlib import md5
import json
import psutil
import sys
import os
import time

lst = []
local_device = []
mobile_device = []
local_number = 0
mobile_number = 0


# 读取JSON文件
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# 将修改后的内容写入JSON文件
def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# 修改指定内容
def update_content(data, key, value, file_path):
    data[key] = value
    write_json(file_path, data)


# 更新usb端口状态
def update_usb():
    tmp_local_number = 0
    tmp_mobile_number = 0
    try:
        part = psutil.disk_partitions()
    except:
        sys.exit()
    for i in range(len(part)):
        tmp_list = part[i].opts.split(',')
        if "fixed" in tmp_list:
            tmp_local_number = tmp_local_number + 1
            local_device.append(part[i].device)
        elif "removable" in tmp_list:
            tmp_mobile_number = tmp_mobile_number + 1
            mobile_device.append(part[i].device)
            pass
        pass
    return [len(part), tmp_local_number, tmp_mobile_number]


# 复制文件
def copy_file(src_path, dst_path, tree):
    dst_path = dst_path + str(int(time.time())) + "\\"
    print(dst_path)
    if tree:
        shutil.copytree(src_path, dst_path)
    else:
        shutil.copy(src_path, dst_path)


# 写入时间戳
def write_time(file_path):
    data = read_json(file_path)
    now_time = int(time.time())
    if data["start_time"] < now_time or data["start_time"] == 0:
        update_content(data, "start_time", int(time.time()), file_path)


# 计算文件md5
def traverse(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            lst.append(os.path.join(root, file))
            for dirr in dirs:
                traverse(dirr)


def create_md5(file):
    m = md5()
    a_file = open(file, 'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
