from aiohttp import web
import aiohttp
import sys 
import asyncio

from type_hints import *
from views import *
from merging import merge
from ip_maker import make_env_ip

from dotenv import dotenv_values

async def debug():
    obj_yandex = await get_data_from_yandex()
    obj_gismeteo = await get_data_from_gismeteo()
    
    merge((obj_yandex, obj_gismeteo))
        
async def get_data(req: aiohttp.ClientRequest) -> aiohttp.ClientResponse:
    obj_yandex = await get_data_from_yandex(req.query)
    obj_gismeteo = await get_data_from_gismeteo(req.query)
    print(obj_gismeteo)
    data = merge((obj_yandex, obj_gismeteo))
    
    return web.json_response(
        data=data, 
        headers={
            "Access-Control-Allow-Origin": "*",
        })

async def get_offline_data(req: aiohttp.ClientRequest) -> aiohttp.ClientResponse:
    data = defaultObj
    return web.json_response(
        data=data,
        headers={
            "Access-Control-Allow-Origin": "*",
        })

if __name__ == '__main__':
    make_env_ip()
    config = dotenv_values("../.env") 
    app = web.Application()
    
    match sys.argv[1]:
        case 'debug':
            print('Starting DEBUG server...')
            asyncio.run(debug())
        case 'offline':
            print('Starting OFFLINE server...')
            app.add_routes([web.get('/', get_offline_data)])
            web.run_app(app, host=config['REACT_APP_SERVER'], port=8000)
        case 'default':
            print('Starting server...')
            app.add_routes([web.get('/', get_data)])
            web.run_app(app, host=config['REACT_APP_SERVER'], port=8000)
            
    asyncio.run(asyncio.sleep(0.1))