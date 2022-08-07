from enum import Enum, auto
from functools import reduce

import json
from date_parsing import keysort_for_DateAlias
from typing import Sequence, Set
from type_hints import *

class WeatherIndexes(Enum):
    sunny = auto()
    cloudly = auto()
    overcloudly = auto()
    low_rain = auto()
    rain = auto()
    hard_rain = auto()
    thunder = auto()

def merge(weather_data_objects: Sequence[WeatherData]) -> JsonAlias:
    
    obj_result = {
        'heading': _find_heading(weather_data_objects),
        'now': _merge_now([obj['now'] for obj in weather_data_objects]),
        'week': _merge_week([obj['week'] for obj in weather_data_objects]),
    }
    
    return json.dumps(obj_result)

def _merge_now(now_objects: Sequence[WeatherDataNow]) -> WeatherDataNow:
    
    length_objects = len([i for i in now_objects])
    now_obj_result = {
        'temperature': sum(obj['temperature'] for obj in now_objects) // length_objects,
        'weather': WeatherIndexes(round(sum(WeatherIndexes[obj['weather']].value for obj in now_objects) / length_objects)).name,
        'humidity': round(sum(obj['humidity'] for obj in now_objects) / length_objects, 2),
        'wind': round(sum(obj['wind'] for obj in now_objects) / length_objects, 1),
        'pressure': sum(obj['pressure'] for obj in now_objects) // length_objects,
    }
    
    return now_obj_result

def _make_set_keys_without_default(week_day_objects: Sequence[WeatherDataWeekDay]) -> Set[str]:
    day_hours = [set(obj.keys()) for obj in week_day_objects]
    set_hours = reduce(lambda res, cur: res & cur, day_hours)
    set_hours -= {'default_temperature', 'default_weather'}
    
    return set_hours

def _merge_week_dayspart(week_day_objects: Sequence[WeatherDataWeekDay]) -> WeatherDataWeekDay:
    day_hours = _make_set_keys_without_default(week_day_objects)
    length_objects = len([i for i in week_day_objects])
    
    dayparts_obj_result = {
        time: {
            'weather': WeatherIndexes(round(sum(WeatherIndexes[obj[time]['weather']].value for obj in week_day_objects) / length_objects)).name,
            'temperature': sum(obj[time]['temperature'] for obj in week_day_objects) // length_objects,
        } for time in day_hours
    }
    
    return dayparts_obj_result

def _merge_week_day(week_day_objects: Sequence[WeatherDataWeekDay]) -> WeatherDataWeekDay:
    length_objects = len([i for i in week_day_objects])
    today_obj_result = {
        'default_temperature': sum(obj['default_temperature'] for obj in week_day_objects) // length_objects,
        'default_weather': WeatherIndexes(round(sum(WeatherIndexes[obj['default_weather']].value for obj in week_day_objects) / length_objects)).name
    }
    today_obj_result.update(_merge_week_dayspart(week_day_objects))
    
    return today_obj_result

def sort_times(times: Sequence[str]) -> Sequence[str]:
    return sorted(times, key=lambda x: int(x.split(':')[0]))

def sort_dayparts(week_day_obj: WeatherDataWeekDay) -> WeatherDataWeekDay:
    result_day_obj = {
        'default_temperature': week_day_obj['default_temperature'],
        'default_weather': week_day_obj['default_weather'],
    }
    
    for part in ('night', 'morning', 'day', 'evening') if 'day' in week_day_obj else sort_times(list(set(week_day_obj.keys()) - {'default_weather', 'default_temperature'})):
        result_day_obj[part] = week_day_obj[part]
    
    return result_day_obj

def _merge_week(week_objects: Sequence[WeatherDataWeek]) -> WeatherDataWeek:
    day_keys = [set(obj.keys()) for obj in week_objects]
    set_keys = reduce(lambda res, cur: res & cur, day_keys)
    
    result = {day: sort_dayparts(_merge_week_day([obj[day] for obj in week_objects])) for day in set_keys}
    result_sorted = {day: result[day] for day in sorted(result, key=keysort_for_DateAlias)}
    return result_sorted

def _find_heading(weather_data_objects: Sequence[WeatherData]) -> str:
    for obj in weather_data_objects:
        if 'heading' in obj:
            return obj['heading']