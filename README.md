# NGA Monitor

[![Build Status](https://travis-ci.org/kcwikizh/nga-monitor.svg?branch=master)](https://travis-ci.org/kcwikizh/nga-monitor)

**监控[NGA](https://bbs.nga.cn)帖子状态**

## 当前监控页面

- [16820397](https://bbs.nga.cn/read.php?tid=16820397) ❌操作失败 47 - 帐号权限不足
- [16334445](https://bbs.nga.cn/read.php?tid=16334445) ❌('Connection broken: IncompleteRead(1477 bytes read, 571 more expected)', IncompleteRead(1477 bytes read, 571 more expected))

## 最后更新时间

2019.07.28 04:39:52

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
