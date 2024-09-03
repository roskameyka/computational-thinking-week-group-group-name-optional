import datetime
import calendar
from translate import Translator

# creating translator object set to translate to Japanese
translator= Translator(to_lang="ja")

def solution_station_2(observation):

    #setting format for converting date string to datetime object
    format = '%Y-%m-%d'

    #converting date string to a datetime object
    dateObject = datetime.datetime.strptime(observation, format)

    #using datetime object to get day of the week as a string in English
    dayOfWeek = calendar.day_name[dateObject.weekday()] 

    #using translator object to translate english string to japanese
    translation = translator.translate(dayOfWeek)

    return translation