import pathlib
import os
parentPath = pathlib.Path(os.path.abspath(__file__)).parent.parent


def check_folder(folder: pathlib.Path):
    if not folder.exists():
        folder.mkdir()

'''
检查文件夹是否存在，不存在则创建
'''
folders = ['log']

for folder in folders:
    path = parentPath / folder
    check_folder(path)

LOG = parentPath / 'log'

