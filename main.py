
import datetime
from datetime import date

def countdown():
    today_date = date.today()
    countdown_year = int(input('Enter the year you want to countdown to in the form YYYY: '))
    countdown_month = int(input('Enter the month you want to countdown to in the form MM: '))
    countdown_day = int(input('Enter the day you want to countdown to in the form DD: '))

    countdown_date = datetime.date(countdown_year, countdown_month, countdown_day)

    time_until_date = abs(countdown_date - today_date)
    print('There are ', time_until_date, ' days to go until ', countdown_date)

countdown()