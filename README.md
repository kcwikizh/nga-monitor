# NGA Monitor

[![Build Status](https://travis-ci.org/kcwikizh/nga-monitor.svg?branch=master)](https://travis-ci.org/kcwikizh/nga-monitor)

**监控[NGA](https://bbs.nga.cn)帖子状态**

## 当前监控页面

- [16334445](https://bbs.nga.cn/read.php?tid=16334445) ❌HTTPSConnectionPool(host='ngabbs.com', port=443): Max retries exceeded with url: /app_api.php?__lib=post&__act=list (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:847)'),))

## 最后更新时间

2020.09.01 08:00:27

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
