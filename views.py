import asyncio
from typing import Hashable
import aiohttp

from type_hints import *
from yandex.linkers import yandex_main_linker

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        return await response.text()

async def get_data_from_yandex(coords: Hashable) -> WeatherData:
    async with aiohttp.ClientSession() as session:
        urls = (
            f'https://yandex.ru/pogoda?lat={coords["lat"]}&lon={coords["lon"]}',
            f'https://yandex.ru/pogoda/details?lat={coords["lat"]}&lon={coords["lon"]}'
        )
        results = await asyncio.gather(*[fetch(session, url) for url in urls])
        
    return yandex_main_linker(*results)