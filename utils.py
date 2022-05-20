import os
import shutil
import numpy as np

import cv2


class MatchFile:
    def __init__(self):
        self.convert2img = False
        self.width = 0
        self.height = 0
        self.frame = 0
        self.dst_path = ""

    def convert_bin_file_to_img(self, file_path, width, height, frame):

        if not os.path.exists(self.dst_path):
            return

        info = os.stat(file_path)
        file_size = info.st_size
        if file_size != width * height * frame:
            return

        f = open(file_path, "rb")
        data = f.read()

        abs_path = os.path.abspath(file_path)
        save_name = file_path.replace(".bin", ".bmp").replace("./", "_")

        for ith_frame in range(self.frame):
            cv2.imwrite(abs_path + ith_frame + save_name, data)

        f.close()


def getfile(work_path, suffix):
    if not suffix:
        return []
    file_list = []
    dir_list = list(os.listdir(work_path))
    for obj in dir_list:
        abs_path = work_path + "/" + obj
        if os.path.isdir(abs_path):
            file_list += getfile(abs_path, suffix)
            continue
        if obj.endswith(suffix):
            # print(obj)
            file_list.append(abs_path)
    return file_list


def copyfile(src_path, dst_path):
    try:
        shutil.copy(src_path, dst_path)
    except Exception as e:
        print("copy error!")
        return


def convert_bin_file_to_img(file_path, width, height, frame):

    info = os.stat(file_path)
    file_size = info.st_size
    if file_size != width * height * frame:
        return

    f = open(file_path, "rb")
    b_data = f.read()
    data = np.frombuffer(b_data, dtype=np.uint8)
    img = data.reshape((frame, height, width))

    abs_path = ''.join(os.path.split(os.path.splitext(file_path)[0])[:-1])
    save_name = file_path.replace(".bin", ".bmp").replace("/", "_").replace(":", "_")

    for ith_frame in range(frame):
        cv2.imwrite(abs_path + "/" + str(ith_frame) + save_name, img[ith_frame])

    f.close()
