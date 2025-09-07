import jdatetime
from hijridate import Hijri

JALALI_HOLIDAYS = {
    (1404, 1, 1), (1404, 1, 2), (1404, 1, 3), (1404, 1, 4),
    (1404, 1, 12), (1404, 1, 13), (1404, 3, 14), (1404, 3, 15),
    (1404, 11, 22), (1404, 12, 29),
}

HIJRI_HOLIDAYS = {kkki
    (1446, 9, 19), (1446, 9, 21), (1446, 9, 23), (1446, 10, 1), (1446, 10, 2),
    (1446, 12, 10), (1446, 12, 18), (1447, 1, 9), (1447, 1, 10), (1447, 2, 20),
    (1447, 2, 28), (1447, 2, 30), (1447, 3, 8), (1447, 3, 17), (1447, 5, 13),
    (1447, 6, 3), (1447, 7, 13), (1447, 7, 27), (1447, 8, 3), (1447, 8, 4),
    (1447, 8, 5), (1447, 8, 15),
}

def is_holiday():
    today_jalali = jdatetime.date.today()
    today_hijri = Hijri.today()

    today_jalali_tuple = (today_jalali.year, today_jalali.month, today_jalali.day)
    today_hijri_tuple = (today_hijri.year, today_hijri.month, today_hijri.day)

    return today_jalali_tuple in JALALI_HOLIDAYS or today_hijri_tuple in HIJRI_HOLIDAYS

def adjust_price(price_str, weekday, holiday):
    price_num = int(price_str.replace(",", ""))
    if holiday:
        price_num = int(price_num * 1.2)
    if weekday in [0, 1]:
        price_num = int(price_num * 0.8)
    return f"{price_num} tomans"