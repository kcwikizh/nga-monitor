#!/usr/bin/env python3
import os


class Config():
    # 监控帖子tid, 可在帖子 URL 找到, 多个 tid 之间使用半角逗号间隔 格式: ‘xxxxx1,xxxxx2’
    NGA_TIDS = os.environ.get('NGA_TIDS') or None
    SLEEP = 0  # seconds 多页面请求等待时间
    LOCAL = os.environ.get('LOCAL') or False  # 本地模式 直接从本地读取文件
    BUILD_PATH = os.path.join(os.path.dirname(__file__), 'build')

    def __init__(self, *args, **kwargs):
        if not self.NGA_TIDS:
            raise Exception('请设置监控帖子 tid NGA_TIDS')
        if isinstance(self.NGA_TIDS, list):
            self.NGA_TIDS = self.NGA_TIDS
        else:
            self.NGA_TIDS = list(
                map(lambda s: s.strip(), filter(lambda s: s, self.NGA_TIDS.split(','))))


config = Config()


if __name__ == "__main__":
    previewConfig = {k: v for k, v in vars(
        config).items() if not k.startswith('__')}
    print(previewConfig)
