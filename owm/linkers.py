from pprint import pprint
import json 

from type_hints import *
from date_parsing import parse_datetime
from owm.setters import owm_weather_setter
from owm.parsers import owm_parse_week

def owm_main_linker(now_obj: JsonAlias, week_obj: JsonAlias) -> WeatherData:
    now_data = _now_linker(now_obj)
    week_data = _week_linker(week_obj)
    
    weather_data = {
        'now': now_data,
        'week': week_data
    }
    
    return weather_data

def _now_linker(now_obj: JsonAlias) -> WeatherDataNow:
    now_obj_parsed = json.loads(now_obj)
    
    obj = {
        'humidity': round(int(now_obj_parsed['main']['humidity'])/100, 2),
        'pressure': int(int(now_obj_parsed['main']['pressure'])*0.75),
        'temperature': int(now_obj_parsed['main']['temp']),
        'weather': owm_weather_setter(now_obj_parsed['weather'][0]['description']),
        'wind': round(int( now_obj_parsed['wind']['speed']), 1)
    }
    
    return obj

def _week_linker(week_obj: JsonAlias) -> WeatherDataWeek:
    week_obj_parsed = json.loads(week_obj)
    
    obj = {
        parse_datetime(item['dt_txt']): {
            'temperature': int(item['main']['temp']),
            'weather': owm_weather_setter(item['weather'][0]['description'])
        } for item in week_obj_parsed['list']
    }
    
    return owm_parse_week(obj)