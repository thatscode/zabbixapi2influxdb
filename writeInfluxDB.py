#!/bin/env python
# -*-coding:utf-8-*-
# import argparse
# import datetime
from influxdb import InfluxDBClient


def write_in(zabbix_data_format):
    host = 'xxxx'
    port = 8086
    user = 'root'
    password = 'xxxx'
    dbname = 'zabbixtest'
    # 需要优化,此处每写一次都需要建立influxdb的连接,效率太低.
    client = InfluxDBClient(host, port, user, password, dbname)
    client.write_points(zabbix_data_format)

if __name__ == '__main__':
    '''
    should fetch from zabbix via WangQuan's item_get API
    type(zabbix_data_format) ----> list
    '''
    zabbix_data_format = [
                {'fields': {
                    'value': 145
                },
                    'tags': {
                            'host': '北京机场主服务器',
                            'site': '北京',
                            'region': '华北飞机场',
                            'type': 'online_clients'
                    },
                    'time': '2015-11-05T07:55:41Z',
                    # 'time': '1446709544',
                    'measurement': 'real_stats_auth'}
    ]

    write_in(zabbix_data_format)



