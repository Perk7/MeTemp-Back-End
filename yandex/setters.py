from type_hints import *

def yandex_weather_now_setter(string: str) -> str:
    if string in ('Облачно с прояснениями', 
                  ):
        return WeatherType['CLOUDLY'].value
    
    if string in ('Пасмурно'):
        return WeatherType['OVERCLOUDLY'].value
    
    if string in ('Ясно'):
        return WeatherType['SUNNY'].value
    
    if string in ('Небольшой дождь',
                  ):
        return WeatherType['LOW_RAIN'].value

    if string in ('Дождь',
                  ):
        return WeatherType['RAIN'].value
    
    return string

def yandex_weather_days_setter(string: str) -> str:
    if string in ('//yastatic.net/weather/i/icons/funky/flat/bkn_d.svg',
                  '//yastatic.net/weather/i/icons/funky/flat/bkn_n.svg',
                  '//yastatic.net/weather/i/icons/funky/dark/bkn_d.svg',
                  '//yastatic.net/weather/i/icons/funky/dark/bkn_n.svg',
                  '/yastatic.net/weather/i/icons/funky/dark/bkn_-ra_n.svg',
                  '//yastatic.net/weather/i/icons/funky/dark/ovc_ra.svg',
                  
                  ):
        return WeatherType['CLOUDLY'].value
    
    if string in ('//yastatic.net/weather/i/icons/funky/flat/skc_d.svg',
                  "//yastatic.net/weather/i/icons/funky/flat/skc_n.svg",
                  '//yastatic.net/weather/i/icons/funky/dark/skc_d.svg',
                  '//yastatic.net/weather/i/icons/funky/dark/skc_n.svg',
                  ):
        return WeatherType['SUNNY'].value
    
    if string in ('//yastatic.net/weather/i/icons/funky/flat/ovc.svg',
                  '//yastatic.net/weather/i/icons/funky/dark/ovc.svg',
                  ):
        return WeatherType['OVERCLOUDLY'].value
    
    if string in ('//yastatic.net/weather/i/icons/funky/dark/ovc_-ra.svg',
                  '//yastatic.net/weather/i/icons/funky/dark/bkn_-ra_d.svg',
                  '//yastatic.net/weather/i/icons/funky/dark/bkn_-ra_n.svg',
                  '//yastatic.net/weather/i/icons/funky/flat/ovc_-ra.svg',
                  '//yastatic.net/weather/i/icons/funky/flat/ovc_ra.svg',
                  '//yastatic.net/weather/i/icons/funky/flat/bkn_-ra_d.svg',
                  ):
        return WeatherType['LOW_RAIN'].value

    if string in ('//yastatic.net/weather/i/icons/funky/dark/bkn_ra_d.svg',
                  '//yastatic.net/weather/i/icons/funky/flat/bkn_ra_d.svg',
                  ):
        return WeatherType['RAIN'].value
    
    if string in ('//yastatic.net/weather/i/icons/funky/dark/bkn_+ra_d.svg',
                  '//yastatic.net/weather/i/icons/funky/dark/ovc_+ra.svg',
                  '//yastatic.net/weather/i/icons/funky/flat/ovc_+ra.svg',
                  ):
        return WeatherType['HARD_RAIN'].value
    
    return string