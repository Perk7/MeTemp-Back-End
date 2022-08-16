import bs4
from type_hints import *
import yandex.parsers as yandex

def yandex_main_linker(now_html: str, week_html: str) -> WeatherData:
    now_data, elem_week_hourly = _now_linker(now_html)
    week_data = _week_linker(week_html, elem_week_hourly)
    
    weather_data = now_data
    weather_data['week'].update(week_data)
    
    weather_data['heading'] = _heading_linker(now_html)
    
    return weather_data

def _now_linker(html_text: str) -> tuple[WeatherData, list[bs4.Tag]]:
    bs = bs4.BeautifulSoup(html_text, 'lxml')
        
    elem_now = bs.select_one('.fact.card.card_size_big')
    
    elem_week_hourly = [i for i in bs.select_one('.forecast-briefly__days').select('.forecast-briefly__day')][2:9]
    
    obj = { 'now': yandex.make_yandex_now(elem_now) }
    obj['week'] = { 'today': yandex.make_yandex_today_hourly(elem_now) }
    obj['week']['today'].update({
        'default_weather': obj['now']['weather'],
        'default_temperature': obj['now']['temperature'] 
    })
    
    return obj, elem_week_hourly

def _week_linker(week_html: str, elem_week_hourly: list[bs4.Tag]) -> WeatherDataWeek:
    bs = bs4.BeautifulSoup(week_html, 'lxml')
    elem_week = [i for i in bs.select('article.card')][2:9]
    
    return yandex.make_yandex_week(elem_week_hourly, elem_week)

def _heading_linker(html: str) -> str:
    bs = bs4.BeautifulSoup(html, 'lxml')
    
    return bs.select_one('#main_title').text