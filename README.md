# NGA Monitor

[![Build Status](https://travis-ci.org/kcwikizh/nga-monitor.svg?branch=master)](https://travis-ci.org/kcwikizh/nga-monitor)

**监控[NGA](https://bbs.nga.cn)帖子状态**

## 当前监控页面

- [法瑟林学院 - 地图配置2.0](https://bbs.nga.cn/read.php?tid=16820397) [✅](16820397.md)

- [16334445](https://bbs.nga.cn/read.php?tid=16334445) ❌('Connection broken: IncompleteRead(0 bytes read)', IncompleteRead(0 bytes read))

## 最后更新时间

2019.07.12 04:29:23

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
