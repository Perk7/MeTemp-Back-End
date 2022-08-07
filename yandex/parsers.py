import bs4
import re

from type_hints import *
import yandex.setters as srs
from date_parsing import parse_date

def make_yandex_now(elem_now: bs4.Tag) -> WeatherDataNow:
    temperature_now = int(elem_now.select_one('.temp.fact__temp.fact__temp_size_s').text)
    weather_now = srs.yandex_weather_now_setter(elem_now.select_one('.link__condition.day-anchor').text)
    humidity_now = round(int(elem_now.select_one('.fact__humidity').select_one('.term__value').text[:-1])/100, 2)
    wind_now = float(elem_now.select_one('.wind-speed').text.replace(',', '.'))
    pressure_now = int(elem_now.select_one('.term.term_orient_v.fact__pressure').select_one('.term__value').text[:3])
    
    return {
        'temperature': temperature_now,
        'weather': weather_now,
        'humidity': humidity_now,
        'wind': wind_now,
        'pressure': pressure_now,
    }
    
def make_yandex_now_hourly(elem_now: bs4.Tag) -> WeatherDataWeekDay:
    elem = elem_now.select_one('[aria-label="Почасовой прогноз"]')
    obj = {}
    new_day = False
    
    for i in elem:
        if any(sub in str(i) for sub in ('sunset', 'sunrise', 'separator')):
            continue
        
        cur_key = i.select_one('.fact__hour-label').text
        if not re.match(r'(\d)?\d:\d\d', cur_key):
            break
        obj[cur_key] = {
            'temperature': int(i.select_one('.fact__hour-temp').text[:-1]),
            'weather': srs.yandex_weather_days_setter(i.select_one('.icon.icon_color_flat.fact__hour-icon')['src']),
        }
        
    return obj

def make_yandex_week(elem_week_hourly: list[bs4.Tag], elem_week: list[bs4.Tag]) -> WeatherDataWeek:
    obj = {}
    
    for i in elem_week_hourly:
        datestamp = i.select_one('.forecast-briefly__date').text
        
        obj[parse_date(datestamp)] = {
            'default_weather': srs.yandex_weather_days_setter(i.select_one('.forecast-briefly__icon')['src']),
            'default_temperature': int(i.select_one('.forecast-briefly__temp_day').text)
        }
        
    dayparts = ['morning', 'day', 'evening', 'night']    
    for i in elem_week:
        datestamp = i.select_one('.a11y-hidden').text.split(',')[1][1:]
        obj[parse_date(datestamp)].update({
            dayparts[ind]: {
                'temperature': sum(map(int, el.select_one('.weather-table__temp').text.split('…')))//2,
                'weather': srs.yandex_weather_days_setter(el.select_one('img')['src'])
            }
            for ind, el in enumerate(i.select('.weather-table__row'))
        })
        
    return obj