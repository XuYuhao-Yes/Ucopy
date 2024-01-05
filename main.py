from PickUpInformation import *
from Template import Template
from Tip import Tip
from Judge import *


template = Template()


if __name__ == "__main__":
    self_examination(template.json_path, template.fields, template.json_template)

    data_json = read_json(template.json_path)
    prompt = data_json["prompt"]
    copy_path = data_json["copy_path"]
    md5_verification = data_json["md5_verification"]
    copy_speed = data_json["copy_speed"]

    data = update_usb()
    now_local_number = 0
    now_mobile_number = 0
    before_number = data[0]
    local_number = data[1]
    mobile_number = data[2]
    now_number = 0

    while True:
        data = update_usb()
        now_number = data[0]
        now_local_number = data[1]
        now_mobile_number = data[2]

        if now_mobile_number > mobile_number:
            if len(mobile_device):
                print("检测到新U盘，正在拷贝...")
                if prompt:
                    tip = Tip("检测到新U盘，正在拷贝...")
                    tip.show()

                if md5_verification:
                    is_copy = judging_files(mobile_device[-1])
                    for i in is_copy:
                        if i != 0:
                            print(i)
                            copy_file(i, copy_path, False)
                else:
                    copy_file(mobile_device[-1], copy_path, True)

                if prompt:
                    tip = Tip("拷贝成功")
                    tip.show()
            before_number = now_number
            local_number = now_local_number
            mobile_number = now_mobile_number
        elif now_mobile_number < mobile_number:
            before_number = now_number
            local_number = now_local_number
            mobile_number = now_mobile_number
        time.sleep(copy_speed)
