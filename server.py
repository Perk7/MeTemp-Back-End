import os
import sys
from aiohttp import web
import aiohttp
import asyncio
import ssl

from type_hints import *
from views import *
from ip_maker import make_env_ip

from dotenv import dotenv_values

async def get_data(req: aiohttp.ClientRequest) -> aiohttp.ClientResponse:
    yandex_obj = await get_data_from_yandex(req.query)
    data = json.dumps(yandex_obj)
    
    return web.json_response(
        data=data, 
        headers={
            "Access-Control-Allow-Origin": "*",
        })
    
if __name__ == '__main__':
    app = web.Application()
    print('Starting server...')
    app.add_routes([web.get('/', get_data)])
    
    if sys.argv[1] == 'local':
        make_env_ip()
        config = dotenv_values("../.env") 
        
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.load_cert_chain(f"./{config['REACT_APP_SERVER']}.pem", f"./{config['REACT_APP_SERVER']}-key.pem")
    
        web.run_app(app, host=config['REACT_APP_SERVER'], port=8000, ssl_context=ssl_context)
    else:
        web.run_app(app, port=os.environ['PORT'])
            
    asyncio.run(asyncio.sleep(0.1))