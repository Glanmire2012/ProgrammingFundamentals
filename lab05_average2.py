#Script: Lab05_average.py
#Author: Owen Sheehan
math_score=float(input('Enter result for Math:'))
english_score=float(input('Enter result for English:'))
science_score=float(input('Enter result for Science:'))
average=((math_score+english_score+science_score)/3)
print('The average Mark was',format(average,'.2f'))
