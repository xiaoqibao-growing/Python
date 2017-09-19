#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 18:41:42
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito
# @Version : 0.1


"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help 显示帮助菜单
    -g        高铁
    -d        动车
    -t        特快
    -k        快速
    -z        直达

Example:
    tickets 北京 上海 2017-10-10
    tickets -dg 成都 南京 2017-10-10

"""

import chardet
import os
import re
import requests
import sys

from docopt import docopt
from pprint import pprint
from prettytable import PrettyTable
from stations import stations


class TrainsCollection(object):
    header = "车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座".split()

    def __init__(self, available_trains, options):
        self.available_trains = available_trains
        self.options = options

    def _get_duration(self, raw_train):
        duration = raw_train.get("lishi").replace(':', "小时") + "分"
        if duration.startswith("00"):
            return duration[4:]
        if duration.startswith("0"):
            return duration[1:]

        return duration

    @property
    def trains(self):
        for raw_train in self.available_trains:
            train_no = raw_train['station_train_code']
            initial = train_no[0].lower()

            if not self.options or initial in self.options:
                train = [
                    train_no,
                    '\n'.join([
                        raw_train['from_station'],
                        raw_train['to_station']
                    ]),
                    '\n'.join([
                        raw_train['start_time'],
                        raw_train['arrive_time']
                    ]),
                    self._get_duration(raw_train),
                    raw_train['zy_num'],
                    raw_train['ze_num'],
                    raw_train['rw_num'],
                    raw_train['yw_num'],
                    raw_train['yz_num'],
                    raw_train['wz_num'],
                ]

                yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)

        for train in self.trains:
            pt.add_row(train)

        print(pt)


def cli():
    arguments = docopt(__doc__)

    stations_decode = {}
    for key, value in stations.items():
        key = key.decode("utf-8")
        stations_decode[key] = value

    from_station = stations_decode.get(arguments["<from>"].decode("windows-1252"))
    to_station = stations_decode.get(arguments["<to>"])
    date = arguments["<date>"]

    url = "https://kyfw.12306.cn/otn/leftTicket/query?"\
        "leftTicketDTO.train_date={}"\
        "&leftTicketDTO.from_station={}"\
        "&leftTicketDTO.to_station={}"\
        "&purpose_codes=ADULT".format(
            date, "BJP", "SHH"
        )

    response = requests.get(url, verify=False)
    result = response.json()['data']['result']

    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])

    TrainsCollection(result, options).pretty_print()


if __name__ == '__main__':
    cli()
    # response = requests.get(
    #     "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?\
    #     station_version=1.9019",
    #     verify=False
    # )

    # stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    # path = os.path.join(os.path.dirname(__file__), "stations.py")

    # print(stations[0][0])
    # pprint(dict(stations.encode("utf-8")), indent=4)
