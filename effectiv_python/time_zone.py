# -*- coding:utf-8 -*-
# __author__ = xuejun

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
