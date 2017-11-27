#!/usr/bin/env python3
import requests
import json
import time
import re
def school():
    path = r'C:\Users\lenovo\Desktop\schools.txt'
    for i in range(2377, 4005):
        for j in range(1, 6):
            url = 'http://xuexiao.ajiao.com/xx/'+str(i)+'-0-0-0-'+str(j)+'/'
            print(url)
            while 1:
                try:
                    req = requests.get(url)
                    break
                except Exception:
                    print(Exception)
                    pass
            text = req.text.replace('\r\n', '').replace(' ','')
            diqu = re.findall('<ahref="http://xuexiao.ajiao.com/xx/.*?<span>(.*?)：</span><label>(.*?)</label>', text, re.S)
            if len(diqu) < 3:
                break
            now_url_next_url = re.findall('class="page-numz-on"(.*?)">.*?class="ui-page-turnpage-next"(.*?)">', text, re.S)
            schools = re.findall('class="bold"href=".*?">(.*?)</a>', text, re.S)
            if len(schools) == 0:
                break
            data = {
                'name': diqu[2][1],
                'schools': schools,
                'juti': diqu,
                'url': url,
            }
            with open(path, 'a', encoding='utf-8') as f:
                print(data, file=f)
            print("ok")
            if now_url_next_url[0][0] == now_url_next_url[0][1]:
                break
    return
school()