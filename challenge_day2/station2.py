import datetime
import calendar
from translate import Translator

translator= Translator(to_lang="ja")

def solution_station_2(observation):

    format = '%Y-%m-%d'

    dateObject = datetime.datetime.strptime(observation, format)

    dayOfWeek = calendar.day_name[dateObject.weekday()] 

    translation = translator.translate(dayOfWeek)

    print(translation)

    return translation