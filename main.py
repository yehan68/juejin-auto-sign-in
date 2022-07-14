# -*- coding: utf-8 -*-
import requests
import os

config = {
  'aid': os.environ.get('AID'),
  'uuid': os.environ.get('UUID'),
  '_signature': os.environ.get('SIGNATURE'),
  'cookie': os.environ.get('COOKIE'),
}

response = requests.post(
  url = 'https://api.juejin.cn/growth_api/v1/check_in?aid=' + config['aid'] + '&uuid=' + config['uuid'] + '&_signature=' + config['_signature'],
  headers = {
    'cookie': config['cookie']
  }
)

if response.status_code == 200:
  result = response.json()
  if result['err_no']:
    print("签到失败: " + result['err_msg'])
  else:
    print('本次签到领取' + str(result['data']['incr_point']) + '钻石')
    print('当前累计为' + str(result['data']['sum_point']) + '钻石')

exit()