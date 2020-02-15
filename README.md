# NGA Monitor

[![Build Status](https://travis-ci.org/kcwikizh/nga-monitor.svg?branch=master)](https://travis-ci.org/kcwikizh/nga-monitor)

**监控[NGA](https://bbs.nga.cn)帖子状态**

## 当前监控页面

- [16334445](https://bbs.nga.cn/read.php?tid=16334445) ❌('Connection broken: IncompleteRead(0 bytes read)', IncompleteRead(0 bytes read))

## 最后更新时间

2020.02.16 06:15:41

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
