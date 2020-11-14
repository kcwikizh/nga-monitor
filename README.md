# NGA Monitor

[![Build Status](https://travis-ci.org/kcwikizh/nga-monitor.svg?branch=master)](https://travis-ci.org/kcwikizh/nga-monitor)

**监控[NGA](https://bbs.nga.cn)帖子状态**

## 当前监控页面

- [16334445](https://bbs.nga.cn/read.php?tid=16334445) ❌("Connection broken: InvalidChunkLength(got length b'', 0 bytes read)", InvalidChunkLength(got length b'', 0 bytes read))

## 最后更新时间

2020.11.14 09:08:20

## 用法

```bash
# 安装依赖
pip install -r requirements.txt
# 修改设置
vim config.py
# 配置监控文章 tid
export NGA_TIDS=xxxxxx
# 运行
python3 main.py
```
