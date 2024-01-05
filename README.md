# Ucopy

> v1.0

> 免责声明: 一旦使用该软件造成任何不良后果,**本人概不负责**

## 1. 简介



该软件可以**自动copy**移动设备中的文件到电脑上

本产品**优点**

- **md5校验**更高的效率和安全
- **安全保护防跟踪**

## 2. 使用方法

> Data.json

``````json
{
    "copy_path": "D:\\U\\",
    "md5_verification": false,
    "self_start": false,
    "prompt": true,
    "md5": [],
    "name": "",
    "copy_speed": 3,
    "start_time": 0
}
``````

- `copy_path`: 拷贝到的位置

- `md5_verification`: md5校验

- `prompt`: 是否启动提示

- `name`: 用户名

- `copy_speed`: 拷贝速度

  > 注意: json文件一旦损坏都会使程序报错

