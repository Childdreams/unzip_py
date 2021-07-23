#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import zipfile

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit("缺少参数")
    file = zipfile.ZipFile(sys.argv[1], "r")
    if os.path.exists(file.namelist()[0]) and os.path.isdir(file.namelist()[0]):
        for root, dirs, files in os.walk(file.namelist()[0], topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.removedirs(os.path.join(root, name))
    for name in file.namelist():
        name1 = str(name.encode("cp437"), encoding="gbk")
        utf8name = name1
        pathname = os.path.dirname(utf8name)
        if not os.path.exists(pathname) and pathname != "":
            os.makedirs(pathname)
        data = file.read(name)
        if not os.path.exists(utf8name):
            fo = open(utf8name, "w", encoding="cp437")
            data = str(data, encoding="cp437")
            fo.write(data)
            fo.close()
    file.close()
