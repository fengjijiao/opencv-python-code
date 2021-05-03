#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests, argparse, send
def main(keyword):
    available = False
    msgStr = "【NCRE成绩发布】\n代查找关键词：" + keyword + "\n"
    r = requests.get('http://search.neea.edu.cn/QueryMarkUpAction.do?act=doQueryCond&pram=certi&community=Home&sid=300')
    if r.status_code == 200:
        msgStr+="获取内容成功!\n查询结果："
        if keyword in r.text:
            available = True
            msgStr+="找到了！"
        else:
            msgStr+="不存在！"
    else:
        msgStr+="获取内容失败，原因：非200"
    return available, msgStr

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyword', type=str, required=True)
    parser.add_argument('--toUser', type=str, required=True)
    args = parser.parse_args()
    available, msgStr = main(args.keyword)
    if available:
         send.message2EWechat(msgStr, args.toUser)