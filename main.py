#!/usr/bin/env python3
import os
import time
import json
import re
import sys
sys.path.append('./lib')

import requests
# pylint: disable=F0401
import html2text
from config import config


def fetchDate(tid: str) -> object:
    resp = requests.post('https://ngabbs.com/app_api.php?__lib=post&__act=list', {'tid': tid}, headers={
                         'X-User-Agent': 'NGA_skull/6.0.5(iPhone10,3;iOS 12.0.1)'})
    if not resp.ok:
        raise Exception('获取数据失败 {}'.format(resp.status_code))
    data = resp.json()
    if data.get('code') != 0:
        raise Exception(
            '操作失败 {} - {}'.format(data.get('code'), data.get('msg')))
    return data


def parseContent(content: str) -> str:
    # content = content.replace('<br/>', '\n')
    # content = re.sub(
    #     '(style|class|cellspacing|rowspan)=("|\').*?("|\')', '', content)
    content = content.replace('点击展开 ...', '')
    content = content.replace('[randomblock]', '')
    content = content.replace('[/randomblock]', '')
    content = content.replace('[quote]', '<q>')
    content = content.replace('[/quote]', '</q>')
    content = content.replace('[list]', '<ul>')
    content = content.replace('[/list]', '</ul>')
    content = re.sub(
        r'\[url\](.*?)\[/url\]', r'<a href="\g<1>" ></a>', content)
    content = re.sub(
        r'\[url=(.*?)\](.*?)\[/url\]', r'<a href="\g<1>" >\g<2></a>', content)
    content = re.sub(
        r'\[img\](.*?)\[/img\]', r'<img src="\g<1>" />', content)
    content = html2text.html2text(content)
    return content


def parseResult(result: object) -> str:
    resultList = ['## #{} {}'.format(result.get(
        'lou'), result.get('author', {}).get('username'))]
    resultList.append(result.get('postdate'))
    resultList.append(parseContent(result.get('content')))
    return '\n\n'.join(map(lambda s: s.strip(), resultList))


def main():
    result = []
    for tid in config.NGA_TIDS:
        print('正在处理 tid={} ...'.format(tid))
        try:
            if config.LOCAL:
                with open(os.path.join(config.BUILD_PATH, '{}.json'.format(tid)), 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = fetchDate(tid)
                data['guest_token'] = '[secure]'
                with open(os.path.join(config.BUILD_PATH, '{}.json'.format(tid)), 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            contents = list(
                map(lambda r: parseResult(r), data.get('result', [])))

            title = '{} - {}'.format(data.get('forum_name'),
                                     data.get('tsubject'))
            # write md
            with open(os.path.join(config.BUILD_PATH, '{}.md'.format(tid)), 'w', encoding='utf-8') as f:
                f.write('# {}\n\n'.format(title))
                f.write('\n---\n\n'.join(contents))
            result.append(
                '- [{title}](https://bbs.nga.cn/read.php?tid={tid}) ✅\n'.format(title=title, tid=tid))
        except Exception as e:
            result.append('{} {}'.format(tid, e))
            print(e)
        time.sleep(config.SLEEP)

    print('处理完成！')
    print('\n'.join(result))
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
        readme = re.sub('(## 当前监控页面\n\n)无', r'\1' + '\n'.join(result), readme)
        readme = re.sub('(## 最后更新时间\n\n)无', r'\g<1>' +
                        time.strftime('%Y.%m.%d %H:%M:%S', time.localtime()), readme)
    with open(os.path.join(config.BUILD_PATH, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme)


if __name__ == '__main__':
    main()
