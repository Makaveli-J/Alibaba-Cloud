#!/usr/bin/env python
#coding=utf-8

from aliyun.log import LogClient, LogItem, GetLogsRequest, IndexConfig
import time
import os

from_time = str(input('Please set start time in the following format\nmm/dd/yyyy or mm/dd/yyyy HH:MM:SS\nStart Time: '))

try:
    from_time = time.mktime(time.strptime(from_time, '%m/%d/%Y'))
except:
    try:
        from_time = time.mktime(time.strptime(from_time, '%m/%d/%Y %H:%M:%S'))
    except:
       print('Invalid Time Format')
       exit()

print('****************************')

to_time = str(input('Please set end time in the following format\nmm/dd/yyyy or mm/dd/yyyy HH:MM:SS\nEnd Time: '))

try:
    to_time = time.mktime(time.strptime(to_time, '%m/%d/%Y'))
except:
    try:
        to_time = time.mktime(time.strptime(to_time, '%m/%d/%Y %H:%M:%S'))
    except:
       print('Invalid Time Format')
       exit()

print('****************************')

print(from_time, to_time)

query1 = '* | SELECT count(*) AS ctr, date_trunc(\'day\', __time__) AS date0 GROUP BY date0 ORDER BY date0 ASC | FROM'
query2 = '{* and status: 405} | SELECT count(*) AS ctr, date_trunc(\'day\', __time__) AS date0 GROUP BY date0 ORDER BY date0 ASC | FROM'
query3 = '* | SELECT real_client_ip, count(*) AS ctr GROUP BY real_client_ip ORDER BY ctr DESC LIMIT 10'
query4 = '{* and status: 405} | SELECT real_client_ip, count(*) AS ctr GROUP BY real_client_ip ORDER BY ctr DESC LIMIT 10'
custom_query = ''

query_selection = {1: query1, 2: query2, 3: query3, 4: query4, 5: custom_query}

print('Select from the following options:')
print('1. Daily Total Requests')
print('2. Daily Blocked Requests')
print('3. Top 10 Source IP')
print('4. Top 10 Blocked Source IP')
print('5. Custom Query')
choice_made = int(input())

client = LogClient('cn-hangzhou.log.aliyuncs.com', os.environ['ACCESS_KEY_ID'], os.environ['ACCESS_KEY_SECRET'])

project_name = 'waf-project-test-cn-hangzhou'

logstore_name = 'waf-test-logstore'

query = query_selection.get(choice_made) + logstore_name

def get_logs():
    print("ready to query logs from logstore %s" % logstore_name)
    request = GetLogsRequest(project_name, logstore_name, from_time, to_time, query=query)
    response = client.get_logs(request)
    for log in response.get_logs():
        for k, v in log.contents.items():
            print("%s : %s" % (k, v))
        print("*********************")

if __name__ == '__main__':
    get_logs()
