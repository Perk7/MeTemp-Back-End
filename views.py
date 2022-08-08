from typing import Hashable
import aiohttp

from type_hints import *
from owm.linkers import owm_main_linker
from yandex.linkers import yandex_main_linker

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

async def get_data_from_yandex(coords: Hashable) -> WeatherData:
    async with aiohttp.ClientSession() as session:
        
        async with session.get(f'https://yandex.ru/pogoda?lat={coords["lat"]}&lon={coords["lon"]}', headers=headers) as resp:
            now = await resp.text()
            
        async with session.get(f'https://yandex.ru/pogoda/details?lat={coords["lat"]}&lon={coords["lon"]}', headers=headers) as resp:
            week = await resp.text()
        
    return yandex_main_linker(now, week)

async def get_data_from_owm(coords: Hashable) -> WeatherData:
    async with aiohttp.ClientSession() as session:
        
        async with session.get(f'https://api.openweathermap.org/data/2.5/weather?lat={coords["lat"]}&lon={coords["lon"]}&appid=158ad2e0f21ac88adc4e43710fa6bdfa&units=metric&lang=ru', headers=headers) as resp:
            now = await resp.text()
            
        async with session.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid=158ad2e0f21ac88adc4e43710fa6bdfa&units=metric&lang=ru', headers=headers) as resp:
            week = await resp.text()
    
    return owm_main_linker(now, week)