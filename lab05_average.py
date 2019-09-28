#Script: lab05_sandwiches.py
#Author: Owen Sheehan
#DEscription: Calculate Sandwich reduction
reduction=(float(input('Enter the percentage of the reduction:'))/100)
original_price=float(input('Enter the original price of the sandwich:'))
new_price=(original_price*(1-reduction))
print('Sandwiches reduced today by',reduction*100,'%',' from €',format(original_price,'.2f'),'to €',format(new_price,'.2f'))