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


import os
import re
import requests

from docopt import docopt
from pprint import pprint
from stations import stations


def cli():
    arguments = docopt(__doc__)
    from_station = stations.get(arguments["<from>"])
    to_station = stations.get(arguments["<to>"])
    date = arguments["<date>"]

    url = "https://kyfw.12306.cn/otn/leftTicket/query?"\
        "leftTicketDTO.train_date={}"\
        "&leftTicketDTO.from_station={}"\
        "&leftTicketDTO.to_station={}"\
        "&purpose_codes=ADULT".format(
            date, from_station, to_station
        )

    response = requests.get(url, verify=False)
    print(response.json())


if __name__ == '__main__':
    cli()
    # response = requests.get(
    #     "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?\
    #     station_version=1.9019",
    #     verify=False
    # )

    # stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    # pprint(dict(stations), indent=4)
