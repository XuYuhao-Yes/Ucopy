# Ucopy
*Translated to English by Fei Gezhu. If there is any mistakes in translating, please just tell **XuYuhao_yes**, I am not responsible for any responsibility.*

> v1.0

## 1. 简介
  ##    Abstract



该软件可以**自动copy**移动设备中的文件到电脑上
*This software can **automaticly copy** the documents and files from the portible devices (such as USB flash disks) to the computers.*

本产品**优点**
The **advantages** of this product:

- **md5校验**更高的效率和安全
  ***MD5 verification** which means higher efficiency and security*
- **安全保护防跟踪**
  ***Security protection with anti tracking***
- 超高**隐蔽性**
  ***Super high concealment***
- 错误自纠
  *Error self correction*

## 2. 使用方法
  ##    Using method

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

- `copy_path: (D:\\U\\)`: 拷贝到的位置 *Place copy to*

- `md5_verification: (true)`: md5校验 *MD5 verification on/off*

- `prompt: (true)`: 是否启动提示 *Starting prompt on/off*

- `name`: 用户名 *Username*

- `copy_speed: (3)`: 拷贝速度 *copy speed*

    >注意: json文件一旦损坏,程序会自动开始纠错,清除所有数据
    >*Note: Once the JSON file is damaged, the software will automatically start correcting errors and clearing all data.*

> 免责声明: 一旦使用该软件造成任何不良后果,**本人概不负责**
> Disclaimer: **I am not responsible for any adverse consequences caused by the use of this software**
