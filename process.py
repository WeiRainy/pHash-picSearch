import sys

from ImageSearch import dhash
from ImageSearch import findImage
import docx

def search(file_path, pic_path):
    # TODO 两个包的路径方法不一样 解决不能使用绝对路径的问题
    # 保存图片的位置
    wd = '../img' if len(sys.argv) < 3 else sys.argv[2]
    # 参数2为保存路径
    findImage.get_pictures(file_path, '../img')
    return dhash.get_result(pic_path, file_path, wd)
