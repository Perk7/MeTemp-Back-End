from aiohttp import web
import aiohttp
import sys 
import asyncio
import ssl
from pprint import pprint

from type_hints import *
from views import *
from merging import merge
from ip_maker import make_env_ip

from dotenv import dotenv_values

async def debug():
    pprint(await get_data_from_owm({
        'lat': 53.983815,
        'lon': 79.238604
    }))
        
async def get_data(req: aiohttp.ClientRequest) -> aiohttp.ClientResponse:
    obj_yandex = await get_data_from_yandex(req.query)
    obj_owm = await get_data_from_owm(req.query)
    data = merge((obj_yandex, obj_owm))
    
    return web.json_response(
        data=data, 
        headers={
            "Access-Control-Allow-Origin": "*",
        })
    
if __name__ == '__main__':
    make_env_ip()
    config = dotenv_values("../.env") 
    
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain('./192.168.1.10.crt', './192.168.1.10.key')
    app = web.Application()
    
    match sys.argv[1]:
        case 'debug':
            print('Starting debug...')
            asyncio.run(debug())
        case 'start':
            print('Starting server...')
            app.add_routes([web.get('/', get_data)])
            web.run_app(app, host=config['REACT_APP_SERVER'], port=8000, ssl_context=ssl_context)
            
    asyncio.run(asyncio.sleep(0.1))