import asyncio
import json
from time import time
from typing import Hashable

from type_hints import *
from views import get_data_from_yandex

async def get_data_with_cache(coords: Hashable) -> WeatherData:
    with open('cache/cache.json', 'r') as f:
        time_now = int(time())
        cache_data = f.read()
        obj = json.loads(cache_data if cache_data else '{}')
        
        if not obj or time_now - obj['expire'] >= 60:
            obj = await make_weather_obj_for_cache(time_now, coords)
            with open('cache/cache.json', 'w') as f:
                f.write(json.dumps(obj))
                
    return json.dumps(obj)
            
async def make_weather_obj_for_cache(time_now: int, coords: Hashable) -> WeatherData:
    data = await get_data_from_yandex(coords)
    if not check_cache_need(data) and not data['week']:
        data['week'] = await get_data_from_yandex(coords)['week']
    data['expire'] = time_now
    
    return data
            
def check_cache_need(data_obj: WeatherData) -> bool:
    return 'day' in list(data_obj['week'].values())[1].keys()