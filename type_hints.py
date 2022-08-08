from enum import Enum
import json
from typing import Literal, TypedDict

TimeAlias = Literal[r'[0-2]\d:[0-6]\d']
JsonAlias = Literal
DateAlias = Literal['today', r'[1-31] [1-12]']
DateTimeAlias = Literal[f'{DateAlias}-{TimeAlias}']

class WeatherType(Enum):
    SUNNY = 'sunny'
    CLOUDLY = 'cloudly'
    OVERCLOUDLY = 'overcloudly'
    LOW_RAIN = 'low_rain'
    RAIN = 'rain'
    HARD_RAIN = 'hard_rain'
    THUNDER = 'thunder'

class WeatherDataNow(TypedDict):
    humidity: float
    pressure: int
    temperature: int
    weather: WeatherType
    wind: float

class WeatherDataWeekDayInfo(TypedDict):
    temperature: int
    weather: WeatherType

WeatherDataWeekDay = dict[Literal['day', 'night', 'evening', 'morning', TimeAlias, 'default_weather', 'default_temperature'], WeatherDataWeekDayInfo]
WeatherDataWeekDateTime = dict[DateTimeAlias, WeatherDataWeekDayInfo]

WeatherDataWeek = dict[DateAlias, WeatherDataWeekDay]

class WeatherData(TypedDict):
    now: WeatherDataNow
    week: WeatherDataWeek
    
defaultObj: JsonAlias = json.dumps({'now': {'humidity': 0.56,
                'pressure': 745,
                'temperature': 23,
                'weather': 'cloudly',
                'wind': 4.0},
            'week': {'today': {'20:00': {'temperature': 23, 'weather': 'cloudly'},
                                '21:00': {'temperature': 22, 'weather': 'cloudly'},
                                '22:00': {'temperature': 20, 'weather': 'cloudly'},
                                'default_temperature': 28,
                                'default_weather': 'sunny',
                                },
                     '10 7': {'default_temperature': 29,
                              'default_weather': 'sunny',
                              'night': {'temperature': 20, 'weather': 'sunny'},
                              'morning': {'temperature': 20, 'weather': 'sunny'},
                              'day': {'temperature': 27, 'weather': 'cloudly'},
                              'evening': {'temperature': 25, 'weather': 'sunny'},
                            },
                    '11 7': {'default_temperature': 29,
                              'default_weather': 'sunny',
                              'night': {'temperature': 20, 'weather': 'sunny'},
                              'morning': {'temperature': 20, 'weather': 'sunny'},
                              'day': {'temperature': 27, 'weather': 'cloudly'},
                              'evening': {'temperature': 25, 'weather': 'sunny'},
                            },
                    '12 7': {'default_temperature': 29,
                              'default_weather': 'sunny',
                              'night': {'temperature': 20, 'weather': 'sunny'},
                              'morning': {'temperature': 20, 'weather': 'sunny'},
                              'day': {'temperature': 27, 'weather': 'cloudly'},
                              'evening': {'temperature': 25, 'weather': 'sunny'},
                            },
                    '13 7': {'default_temperature': 29,
                              'default_weather': 'sunny',
                              'night': {'temperature': 20, 'weather': 'sunny'},
                              'morning': {'temperature': 20, 'weather': 'sunny'},
                              'day': {'temperature': 27, 'weather': 'cloudly'},
                              'evening': {'temperature': 25, 'weather': 'sunny'},
                            },
                    '14 7': {'default_temperature': 29,
                              'default_weather': 'sunny',
                              'night': {'temperature': 20, 'weather': 'sunny'},
                              'morning': {'temperature': 20, 'weather': 'sunny'},
                              'day': {'temperature': 27, 'weather': 'cloudly'},
                              'evening': {'temperature': 25, 'weather': 'sunny'},
                            },
                    '15 7': {'default_temperature': 29,
                              'default_weather': 'sunny',
                              'night': {'temperature': 20, 'weather': 'sunny'},
                              'morning': {'temperature': 20, 'weather': 'sunny'},
                              'day': {'temperature': 27, 'weather': 'cloudly'},
                              'evening': {'temperature': 25, 'weather': 'sunny'},
                            },
                    '16 7': {'default_temperature': 29,
                              'default_weather': 'sunny',
                              'night': {'temperature': 20, 'weather': 'sunny'},
                              'morning': {'temperature': 20, 'weather': 'sunny'},
                              'day': {'temperature': 27, 'weather': 'cloudly'},
                              'evening': {'temperature': 25, 'weather': 'sunny'},
                            },
                    }
    })