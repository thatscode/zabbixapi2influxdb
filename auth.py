#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
import sys
class zabbixtools:
    def __init__(self):
        self.url = "http://123.56.22.43/zabbix/api_jsonrpc.php"
        self.header = {"Content-Type": "application/json"}
        self.authID = self.user_login()
	#self.argv = sys.argv[1]
    def user_login(self):
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "user.login",
                    "params": {
                        "user": "admin",
                        "password": "airport453"
                        },
                    "id": 0
                    })
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print "Auth Failed, Please Check Your Name And Password:",e.code
        else:
            response = json.loads(result.read())
            result.close()
            authID = response['result']
            #print authID
            return authID
    def get_data(self,data,hostip=""):
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
            return 0
        else:
            response = json.loads(result.read())
            result.close()
            return response
    def hostgroup_get(self):
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "hostgroup.get",
                    "params": {
                        "output": "extend",
                        },
                    "auth": self.authID,
                    "id": 1,
                    })
        res = self.get_data(data)
        if 'result' in res.keys():
            res = res['result']
            if (res !=0) or (len(res) != 0):
                print "\033[1;32;40m%s\033[0m" % "Number Of Group: ", "\033[1;31;40m%d\033[0m" % len(res)
                for group in res:
                    print "\t","HostGroup_id:",group['groupid'],"\t","HostGroup_Name:",group['name'].encode('utf-8')
                print
        else:
            print "Get HostGroup Error,please check !"
    def hostid_get(self):
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output": "extend",
                        },
                    "auth": self.authID,
                    "id": 1,
                    })
        res = self.get_data(data)
        if 'result' in res.keys():
            res = res['result']
            if (res !=0) or (len(res) != 0):
                print "\033[1;32;40m%s\033[0m" % "Host_id: ", "\033[1;31;40m%d\033[0m" % len(res)
                for host in res:
                    print "\t","Host_id:",host['hostid'],"\t","Host_Name:",host['name'].encode('utf-8')
                print
        else:
            print "Get Host_id Error,please check !"
    def itemid_get(self):
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "item.get",
                    "params": {
                        "output": "extend",
                        #"output":["itemids","key_","hostid","templateid"],
                        "host":"nanjingAC"
                        },
                    "auth": self.authID,
                    "id": 1,
                    })
        res = self.get_data(data)
        if 'result' in res.keys():
            res = res['result']
            if (res !=0) or (len(res) != 0):
                print "\033[1;32;40m%s\033[0m" % "Itemids: ", "\033[1;31;40m%d\033[0m" % len(res)
                for itemid in res:
                    print itemid
                    #print "\t","Host_id:",host['hostid'],"\t","Host_Name:",host['name'].encode('utf-8')
                print
        else:
            print "Get Host_id Error,please check !"
    def history_get(self):
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "history.get",
                    "params": {
                        "output":"extend",
                        "history":3,
                        "itemids":30359,
                        "limit":1,
                        #"time_from":1447211471
                        #"time_till":1452481871
                        },
                    "auth": self.authID,
                    "id": 1,
                    })
        res = self.get_data(data)
        if 'result' in res.keys():
            res = res['result']
            if (res !=0) or (len(res) != 0):
                #print "\033[1;32;40m%s\033[0m" % "Host_id: ", "\033[1;31;40m%d\033[0m" % len(res)
                for history in res:
                    history['site'] = '北京机场'
                    history['region'] = '华北机场'
                    history['host'] = '主服务器'
                    history['type'] = 'AP终端关联数量'
                    history['measurement'] = 'real_stats_auth'
                    history.pop('ns')
                    history.pop("itemid")
                    str(history).decode('utf8')
                    print history
                    #print "\t","Host_id:",host['hostid'],"\t","Host_Name:",host['name'].encode('utf-8')
                print
        else:
            print "Get Host_id Error,please check !"
def main():
    test = zabbixtools()
    #test.hostgroup_get()
    #test.hostid_get()
    #test.itemid_get()
    test.history_get()
if __name__ == "__main__":
    main()
