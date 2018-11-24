#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/8/28  
# @Author  : 冷冠男
# @File    : qiang  
# @Description :登录
#
#
import requests


def get_cookies():
    """
    获得cookies
    :return: 
    """
    url = 'http://xuanzuo.hrbcu.edu.cn/roompre/default.aspx?tdsourcetag=s_pctim_aiomsg'
    s = requests.session()
    s.get(url)
    ck_dict = requests.utils.dict_from_cookiejar(s.cookies)     # 将jar格式转化为dict
    ck = 'ASP.NET_SessionId=' + ck_dict['ASP.NET_SessionId'] + "; safedog-flow-item="               # 重组cookies
    return ck


def login(cookies):
    """
    登录
    :param cookies: 
    :return: 
    """
    login_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '45',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies,
        'Host': 'xuanzuo.hrbcu.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://xuanzuo.hrbcu.edu.cn/roompre/?tdsourcetag=s_pctim_aiomsg',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    }
    login_url = 'http://xuanzuo.hrbcu.edu.cn/roompre/default.aspx?tdsourcetag=s_pctim_aiomsg'
    login_data = {
        '__EVENTVALIDATION': '/wEWBALZ78aDBALs0bLrBgLs0fbZDALXyuyUCQfGqE8JhEv26pfSwoizgtkSUOA7',
        '__VIEWSTATE': '/wEPDwUKMTgxOTM2MzEwNQ9kFgICAw9kFgICAQ9kFgJmDw8WAh4EVGV4dAUw5ZOI5bCU5ruo5ZWG5Lia5aSn5a2m5Zu+5Lmm6aaG5bqn5L2N6aKE57qm57O757ufZGRkgBENHUIL88+7ogjOyGKtQH3kG/c=',
        'Button_ok': '确定',
        'TextBox1': '201523020516',
        'TextBox2': '970722',
    }
    res = requests.post(login_url, data=login_data, headers=login_headers)
    #print(res.text)


def selection_area(cookies, areas, seat_1, seat_2):
    """
    选座
    :param cookies: 
    :param areas: 输入例子为：'22' 楼层区域 [22：一楼大厅自习区[80], 23:二楼北侧自习区[196], 24:二楼经济书库自习区[88], 25:二楼社科书库自习区[120], 
    27:三楼北侧自习区[79], 28:三楼东侧自习区[74], 29:三楼工具书库自习区[76], 30:三楼科技书库自习区[276], 31:三楼南侧自习区[112],
    32:三楼西侧自习区[70], 33:三楼样本书库自习区[88], 34:四楼北侧自习区[144], 35:四楼东侧自习区[70], 36:四楼南侧自习区[116],
    37:四楼西侧自习区[74], 38:四楼中文过刊阅览室[288], 39:四东室内自习区[452], 40:五楼东侧自习区[70], 41:五楼南侧自习区[120],
    42:五楼西侧自习区[64], 43:五西室内自习区[0], 44:三楼经典图书阅览室[72]]
    :param seat_1: 输入例子为：1
    :param seat_2: 输入例子为：001 三位数字，不够前面补0
    :return:
    """
    selection_headers = {

        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '8087',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies,
        'X-MicrosoftAjax': 'Delta=true',
        'Host': 'xuanzuo.hrbcu.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://xuanzuo.hrbcu.edu.cn/roompre/Default.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    }
    selection_area_url = 'http://xuanzuo.hrbcu.edu.cn/roompre/ReaderLook.aspx'
    temp = areas+'_'+seat_1+'_6_0_'+seat_2+'_d'
    selection_data = {
        '__EVENTARGUMENT': (eval(seat_1) - 1),
        '__EVENTTARGET': 'imageM',
        '__EVENTVALIDATION': '/wEWBALysKvUAgKE2ZuoAwLZ2ou6CgKqoYLkCOjylEvLK4LWQJWQfXQmXU9t+SPj',
        '__VIEWSTATE': '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BQ0yMl8xNl82XzBfMDE2FgYfCwUfNTUxLDI1OSw1ODMsMjU5LDU4MywyOTQsNTUxLDI5NB8MCysEAh8NBQ0yMl8xN182XzBfMDE3FgYfCwUfNTUyLDI5Niw1ODUsMjk2LDU4NSwzMjksNTUyLDMyOR8MCysEAh8NBQ0yMl8xOF82XzBfMDE4FgYfCwUfNTk4LDI1OCw2MzAsMjU4LDYzMCwyOTQsNTk4LDI5NB8MCysEAh8NBQ0yMl8xOV82XzBfMDE5FgYfCwUfNTk5LDI5Nyw2MzEsMjk3LDYzMSwzMjcsNTk5LDMyNx8MCysEAh8NBQ0yMl8yMF82XzBfMDIwFgYfCwUfNjM2LDI1OSw2NzAsMjU5LDY3MCwyOTQsNjM2LDI5NB8MCysEAh8NBQ0yMl8yMV82XzBfMDIxFgYfCwUfNjM2LDI5Niw2NjksMjk2LDY2OSwzMjYsNjM2LDMyNh8MCysEAh8NBQ0yMl8yMl82XzBfMDIyFgYfCwUfNjgxLDI1Nyw3MTYsMjU3LDcxNiwyOTQsNjgxLDI5NB8MCysEAh8NBQ0yMl8yM182XzBfMDIzFgYfCwUfNjgyLDI5Niw3MTcsMjk2LDcxNywzMjcsNjgyLDMyNx8MCysEAh8NBQ0yMl8yNF82XzBfMDI0FgYfCwUfNzIyLDI2MCw3NTQsMjYwLDc1NCwyOTQsNzIyLDI5NB8MCysEAh8NBQ0yMl8yNV82XzBfMDI1FgYfCwUfNzIyLDI5Niw3NTMsMjk2LDc1MywzMjQsNzIyLDMyNB8MCysEAh8NBQ0yMl8yNl82XzBfMDI2FgYfCwUfNzY5LDI2MCw4MDEsMjYwLDgwMSwyOTQsNzY5LDI5NB8MCysEAh8NBQ0yMl8yN182XzBfMDI3FgYfCwUfNzY3LDI5Niw4MDAsMjk2LDgwMCwzMjYsNzY3LDMyNh8MCysEAh8NBQ0yMl8yOF82XzBfMDI4FgYfCwUfODA2LDI1OCw4MzgsMjU4LDgzOCwyOTQsODA2LDI5NB8MCysEAh8NBQ0yMl8yOV82XzBfMDI5FgYfCwUfODA2LDI5Niw4MzgsMjk2LDgzOCwzMjUsODA2LDMyNR8MCysEAh8NBQ0yMl8zMF82XzBfMDMwFgYfCwUfODUxLDI1OCw4ODcsMjU4LDg4NywyOTQsODUxLDI5NB8MCysEAh8N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',
        temp : '确定',
        'ScriptManager1': 'UpdatePanel1|'+temp,
    }
    res = requests.post(selection_area_url, data=selection_data, headers=selection_headers )
    print(res.text)


def main():
    ck = get_cookies()
    login(ck)
    selection_area(ck, '22', '3', '003')


if __name__ == '__main__':
    main()