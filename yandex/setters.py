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
    string = string.removeprefix('//yastatic.net/weather/i/icons/funky/')
    
    if string in ('flat/skc_d.svg',
                  "flat/skc_n.svg",
                  'dark/skc_d.svg',
                  'dark/skc_n.svg',
                  ):
        return WeatherType['SUNNY'].value
    
    if string in ('flat/bkn_d.svg',
                  'flat/bkn_n.svg',
                  'dark/bkn_d.svg',
                  'dark/bkn_n.svg',
                  ):
        return WeatherType['CLOUDLY'].value
    
    if string in ('flat/ovc.svg',
                  'dark/ovc.svg',
                  'dark/bkn_-ra_n.svg',
                  'flat/bkn_-ra_n.svg',
                  'dark/bkn_-ra_d.svg',
                  'flat/bkn_-ra_d.svg',
                  ):
        return WeatherType['OVERCLOUDLY'].value
    
    if string in ('dark/ovc_-ra.svg',
                  'flat/ovc_-ra.svg',
                  'dark/bkn_ra_d.svg',
                  'flat/bkn_ra_d.svg',
                  'dark/bkn_ra_n.svg',
                  'flat/bkn_ra_n.svg',
                  ):
        return WeatherType['LOW_RAIN'].value

    if string in ('flat/ovc_ra.svg',
                  'dark/ovc_ra.svg',
                  'dark/bkn_+ra_d.svg',
                  'flat/bkn_+ra_d.svg',
                  'dark/bkn_+ra_n.svg',
                  'flat/bkn_+ra_n.svg',
                  ):
        return WeatherType['RAIN'].value
    
    if string in ('dark/ovc_+ra.svg',
                  'flat/ovc_+ra.svg',
                  ):
        return WeatherType['HARD_RAIN'].value
    
    return string