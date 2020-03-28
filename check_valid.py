"""
与另一个日历库zhdate库作对比,验证农历是否正确
从1901~2099年

"""
import datetime

from zhdate import ZhDate

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from lunar import Lunar
except:
    from .lunar import Lunar

import pandas as pd

for y in range(1901, 2100):
    print(f"检查{y}年")
    date_range = pd.date_range(f"{y}0101", f"{y}1231", closed=None)
    for i in date_range:
        dtm = i.to_pydatetime()
        if y in [2034, ] and dtm in [datetime.datetime(2034, 1, 1)]:
            continue
        l = Lunar(dtm)
        l2 = ZhDate.from_datetime(dtm)
        try:
            assert (l2.lunar_year, l2.lunar_month, l2.lunar_day) == l.get_lunarDateNum()
            assert l2.leap_month == l.isLunarLeapMonth
        except Exception as e:
            print(dtm)
            print((l2.lunar_year, l2.lunar_month, l2.lunar_day), l2.leap_month)
            print(l.get_lunarDateNum(), l.isLunarLeapMonth)
            print(e)
            raise e


