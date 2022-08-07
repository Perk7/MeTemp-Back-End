from type_hints import *
from typing import Sequence

def parse_date(timestamp: str) -> DateAlias:
    splitted_date: Sequence[str] = timestamp.split()
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    months_short = ['янв', 'фев', 'марта', 'апр', 'мая', 'июня', 'июля', 'авг', 'сен', 'окт', 'нояб', 'дек']
    
    splitted_date[1] = str((months if splitted_date[1] in months else months_short).index(splitted_date[1])+1)
            
    result: DateAlias = ' '.join(splitted_date)
    return result

def keysort_for_DateAlias(date: DateAlias) -> int:
    if date == 'today':
        return 0
    return int(date.split()[1])*1000 + int(date.split()[0])