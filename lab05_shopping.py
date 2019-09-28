#Script: lab05_shopping.py
#Author: Owen Sheehan
price_milk=float(input('Enter the price of milk:'))
price_bread=float(input('Enter the price of Bread:'))
amount_milk=int(input('Enter the no. of litres bought:'))
amount_bread=int(input('enter the no. of loaves bought:'))
print('Your Bill')
print('-----------')
print('Milk\t\t',amount_milk,'\t\t',price_milk,'\t',(price_milk*amount_milk))
print('Bread\t\t',amount_bread,'\t\t',price_bread,'\t',(price_bread*amount_bread))
print('--------------------------------------------')
total=(price_milk*amount_milk)+(price_bread*amount_bread)
print('Total\t\t\t\t\t\t',total)
print('Final Cost\t\t\t\t\t',(total*.9))