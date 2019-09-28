#Script= lab05_computing
#Author : Owen Sheehan
no_of_days_a_week=float(5)
no_of_weeks_worked=float(46)
no_of_days_a_year=(no_of_days_a_week*no_of_weeks_worked)
name=input('Enter you name:')
daily_minutes=float(input('Enter the time in minutes that you travel daily:'))
daily_distance=float(input('Enter the distance you travel:'))
print('You will travel a total of',(daily_distance*no_of_days_a_year),'Km,')
total_time_mins=(daily_minutes*no_of_days_a_year)
print('Time spent travelling in one year is',total_time_mins,'minutes')
hours=((total_time_mins//60)%24)
days=((total_time_mins//60)//24)
minutes=(total_time_mins%60)
print('This is the equialent of',format(days,'.0f'),'days',format(hours,'.0f'),'hours',format(minutes,'.0f'),'minutes')

