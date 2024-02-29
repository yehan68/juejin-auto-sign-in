# -*- coding: utf-8 -*-
import requests
import os

config = {
  'aid': os.environ.get('AID'),
  'uuid': os.environ.get('UUID'),
  '_signature': os.environ.get('SIGNATURE'),
  'cookie': os.environ.get('COOKIE'),
}

# 沾喜气接口已经下线
# dipResponse = requests.post(
#   url = 'https://api.juejin.cn/growth_api/v1/lottery_lucky/dip_lucky?aid=' + config['aid'] + '&uuid=' + config['uuid'] + '&spider=0',
#   headers = {
#     'cookie': config['cookie']
#   }
# )

# if dipResponse.status_code == 200:
#   dipResult = dipResponse.json()
#   if dipResult['err_no']:
#     print("签到失败: " + dipResult['err_msg'])
#     print('本次沾喜气获得' + str(dipResult['data']['dip_value']) + '幸运值')
#     print('当前累计幸运值为' + str(dipResult['data']['total_value']))
#   else:
#     print('本次沾喜气获得' + str(dipResult['data']['dip_value']) + '幸运值')
#     print('当前累计幸运值为' + str(dipResult['data']['total_value']))

checkResponse = requests.post(
  url = 'https://api.juejin.cn/growth_api/v1/check_in?aid=' + config['aid'] + '&uuid=' + config['uuid'] + '&_signature=' + config['_signature'],
  headers = {
    'cookie': config['cookie']
  }
)

if checkResponse.status_code == 200:
  checkResult = checkResponse.json()
  if checkResult['err_no']:
    print("签到失败: " + checkResult['err_msg'])
  else:
    print('本次签到领取' + str(checkResult['data']['incr_point']) + '钻石')
    print('当前累计为' + str(checkResult['data']['sum_point']) + '钻石')

exit()