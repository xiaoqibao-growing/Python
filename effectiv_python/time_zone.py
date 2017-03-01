# -*- coding:utf-8 -*-
# __author__ = xuejun

"""
    zh:我们应该在返回的日期中添加时区信息，任何没有时区的日期我个人认为都是一个BUG。
    en:We should add time zone in time returned, any date has no time zone I personally think is a BUG.
"""

from datetime import datetime
from datetime import tzinfo
import pytz


def utcnow():
    return datetime.now(tz=pytz.utc)

if __name__ == '__main__':
    print datetime.utcnow()
    print datetime.now()
    print utcnow()
    print utcnow().isoformat()
