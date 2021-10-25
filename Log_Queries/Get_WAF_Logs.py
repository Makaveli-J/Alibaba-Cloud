#!/usr/bin/env python
#coding=utf-8

from aliyun.log import LogClient, LogItem, GetLogsRequest, IndexConfig
import time
import os
import Set_Time
import Validate_Selection

# set time range for the log query
time_range = Set_Time.get_time()

from_time = time_range[0]
to_time = time_range[1]

# define WAF log queries
query1 = '* | SELECT count(*) AS ctr, date_trunc(\'day\', __time__) AS date0 GROUP BY date0 ORDER BY date0 ASC | FROM '
query2 = '{* and status: 405} | SELECT count(*) AS ctr, date_trunc(\'day\', __time__) AS date0 GROUP BY date0 ORDER BY date0 ASC | FROM '
query3 = '* | SELECT real_client_ip, count(*) AS ctr GROUP BY real_client_ip ORDER BY ctr DESC LIMIT 10 | FROM '
query4 = '{* and status: 405} | SELECT real_client_ip, count(*) AS ctr GROUP BY real_client_ip ORDER BY ctr DESC LIMIT 10 | FROM '
custom_query = ''

query_selection = {1: query1, 2: query2, 3: query3, 4: query4, 5: custom_query}

# Select log query
print('Select from the following options:')
print('1. Daily Total Requests')
print('2. Daily Blocked Requests')
print('3. Top 10 Source IP')
print('4. Top 10 Blocked Source IP')
print('5. Custom Query')
choice_made = input()

while Validate_Selection.validate_selection(choice_made, len(query_selection)+1) is False:
    choice_made = input('Invalid input, please try again\n')
    Validate_Selection.validate_selection(choice_made, len(query_selection)+1)

choice_made = int(choice_made)

client = LogClient('cn-hangzhou.log.aliyuncs.com', os.environ['ACCESS_KEY_ID'], os.environ['ACCESS_KEY_SECRET'])

project_name = 'waf-project-test-cn-hangzhou'

logstore_name = 'waf-test-logstore'

if choice_made in range(1, 5):
    query = query_selection.get(choice_made) + logstore_name
else:
    query = input('Please enter custom query:\n') + ' | FROM ' + logstore_name


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
