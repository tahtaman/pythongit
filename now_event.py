'''
-------------------------------------------------
Documentation for module now_event.py
-------------------------------------------------
'''
import datetime

#'''
quest = 'WC FIS ski 4x5km'
quest_start_day = 7
quest_start_hour = 15
quest_start_minute = 20
quest_end_hour = 16
quest_end_minute = 30
#'''

now = datetime.datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

today = now.day
now_time = '{0}/{1}/{2} {3:02d}:{4:02d}'.format(day, month, year, hour, minute)

def display_now_events(event_date, event_hour_start, event_min_start,
                       event_hour_end, event_min_end, quest):
    '''
    ------------------------------------------------
    Documentation for function display_now_events().
    ------------------------------------------------
    '''
    #переводим получаемое время в десятичный вид
    event_hour_start = event_hour_start + event_min_start/60
    event_hour_end = event_hour_end + event_min_end/60

    #переводим текущее время в десятичный вид
    now_time_dec = now.hour + now.minute/60

    ####
    #print(event_hour_start, event_hour_end)

    #проверяем день
    if event_date == now.day:
        #проверяем происходит ли событие сейчас
        if event_hour_start <= now_time_dec and event_hour_end >= now_time_dec:
            return print('Now {0} - {1}'.format(now_time, quest))
        else: return print('no events now time')
    else: return print('No events today')

print(display_now_events(quest_start_day, quest_start_hour, quest_start_minute,
                         quest_end_hour, quest_end_minute, quest))
