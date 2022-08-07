from typing import Hashable
import aiohttp

from type_hints import *
from yandex.linkers import yandex_main_linker
from gismeteo.linkers import gismeteo_main_linker, gismeteo_recieve_url

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

async def get_data_from_yandex(coords: Hashable) -> WeatherData:
    async with aiohttp.ClientSession() as session:
        
        async with session.get(f'https://yandex.ru/pogoda?lat={coords["lat"]}&lon={coords["lon"]}', headers=headers) as resp:
            now = await resp.text()
            
        async with session.get(f'https://yandex.ru/pogoda/details?lat={coords["lat"]}&lon={coords["lon"]}', headers=headers) as resp:
            week = await resp.text()
        
    return yandex_main_linker(now, week)

async def get_data_from_gismeteo(coords: Hashable) -> WeatherData:
    
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.gismeteo.ru/', headers=headers) as resp:
            resp = await resp.text()
            url = gismeteo_recieve_url(resp)
        
        async with session.get(f'{url}/now/', headers=headers) as resp:
            now = await resp.text()
        
        async with session.get(f'{url}/', headers=headers) as resp:
            today = await resp.text()
            
        async with session.get(f'{url}/3-days/', headers=headers) as resp:
            week = await resp.text()
            
        async with session.get(f'{url}/10-days/', headers=headers) as resp:
            week_default = await resp.text()
    
    return gismeteo_main_linker(now, today, week, week_default)