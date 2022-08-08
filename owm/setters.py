from type_hints import *

def owm_weather_setter(string: str) -> str:
    if string in ("облачно с прояснениями",
                  "переменная облачность",
                  "небольшая облачность", 
                  ):
        return WeatherType['CLOUDLY'].value
    
    if string in ("пасмурно"):
        return WeatherType['OVERCLOUDLY'].value
    
    if string in ("ясно"):
        return WeatherType['SUNNY'].value
    
    if string in ("небольшой дождь",
                  ):
        return WeatherType['LOW_RAIN'].value

    if string in ("дождь",
                  ):
        return WeatherType['RAIN'].value
    
    return string