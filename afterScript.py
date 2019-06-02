#!/usr/bin/env python3
import os
import hashlib
from shutil import copyfile

from config import config

OLD_BUILD_PATH = os.path.join(os.path.dirname(__file__), 'old_build')

def main():
    if not os.path.isdir(OLD_BUILD_PATH):
        print('未发现旧构建目录，跳过检查')
        return
    if not os.path.isdir(config.BUILD_PATH):
        raise Exception('未发现构建目录!!')
    oldFiles = list(filter(lambda filename: filename.split('.')
                           [-1] == 'md' and filename != 'README.md', os.listdir(OLD_BUILD_PATH)))
    newFiles = list(filter(lambda filename: filename.split('.')
                           [-1] == 'md'  and filename != 'README.md', os.listdir(config.BUILD_PATH)))
    flag = False
    for oldF in oldFiles:
        if not os.path.exists(os.path.join(config.BUILD_PATH, oldF)):
            copyfile(os.path.join(OLD_BUILD_PATH, oldF),
                     os.path.join(config.BUILD_PATH, oldF))
            flag = True
            print('未发现新构建文件 {}，复制旧文件（如TIDS列表有增减，请清理CI缓存）'.format(oldF))
    for newF in newFiles:
        if not os.path.exists(os.path.join(OLD_BUILD_PATH, newF)):
            print('发现新构建文件 {}'.format(newF))
            flag = True
    if flag:
        print('存在文件变动或存在失败构建，将部署新构建')
        return
    print('正在对比新旧文件。。。')
    for newF in newFiles:
        newMd5 = hashlib.md5(open(os.path.join(config.BUILD_PATH, newF),'rb').read()).hexdigest()
        oldMd5 = hashlib.md5(open(os.path.join(OLD_BUILD_PATH, newF),'rb').read()).hexdigest()
        if newMd5 != oldMd5 :
            flag = True
            print('{} 文件有改动'.format(newF))
    if flag:
        print('存在文件变动，将部署新构建')
        return
    print('不存在文件变动，将使用旧时间戳部署')
    copyfile(os.path.join(OLD_BUILD_PATH, 'README.md'), os.path.join(config.BUILD_PATH, 'README.md'))

if __name__ == "__main__":
    main()
