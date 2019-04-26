# NGA Monitor

[![Build Status](https://travis-ci.org/kcwikizh/nga-monitor.svg?branch=master)](https://travis-ci.org/kcwikizh/nga-monitor)

**监控[NGA](https://bbs.nga.cn)帖子状态**

## 当前监控页面

- [舰队collection - [罗盘娘攻略度：51.3%]梦美的常规图带路 &amp; 出击配置 v2[妖精施工中……]](https://bbs.nga.cn/read.php?tid=16334445) ✅


## 最后更新时间

2019.04.27 04:49:48

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
