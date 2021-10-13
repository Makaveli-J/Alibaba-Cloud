#!/usr/bin/env python
#coding=utf-8

import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.RevokeSecurityGroupRequest import RevokeSecurityGroupRequest

client = AcsClient(os.environ['ACCESS_KEY_ID'], os.environ['ACCESS_KEY_SECRET'], 'cn-hangzhou')

request = RevokeSecurityGroupRequest()
request.set_accept_format('json')

request.set_IpProtocol('tcp')
request.set_SourceCidrIp('10.0.0.0/8')
request.set_Description('test')

#Security Group List
sg_lst = ['sg-test', 'sg-test0']
lst_p = ['20/22', '80/80', '443/443']

#For Loop to delete rules
for i in sg_lst:
    for p in lst_p:
        request.set_PortRange(p)
        request.set_SecurityGroupId(i)
        response = client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'), i, p)
