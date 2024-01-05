"""
!/usr/bin/python11
-*- coding: utf-8 -*-            
@Author : xuyuhao
@Time : 2023/12/29 22:22
@FileName: Template.py
"""


class Template:
    def __init__(self, false=False, true=True):
        self.json_template = {
            "copy_path": "D:\\U\\",
            "md5_verification": true,
            "self_start": false,
            "prompt": true,
            "md5": [],
            "name": "",
            "copy_speed": 5,
            "start_time": 0
        }

        self.json_path = "./Data.json"
        self.fields = ["self_start", "prompt", "copy_path", "md5_verification", "md5", "name", "start_time",
                       "copy_speed"]
