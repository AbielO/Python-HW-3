import os
import csv

number_months = 0
profit = 0
i = 0
row = 0

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    
    ch = []
    next(csvfile)
    for row in csvreader:
        profit += float(row[1])
        
        convert = float(row[1])
        pl= ch.append(convert)
        number_months = number_months + 1
        max_profit = round(max(ch), 2)
        max_loss = round(min(ch), 2)
        import statistics 
        average = round(statistics.mean(ch), 2)
    
        

    

print('Financial Analysis')
print('--------------------------')

print(f'Total Months: {number_months}')
print(f'Total: ${profit}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: ${max_profit}')
print(f'Greatest Decrease in Profits:: ${max_loss}')


with open("Budget_Analysis", "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("--------------------------" + "\n")
    text.write("f'Total Months: {number_months}'" + "\n")
    text.write("f'Total: ${profit}'" + "\n")
    text.write("f'Average Change: ${average}'" + "\n")
    text.write("f'Greatest Increase in Profits: ${max_profit}'" + "\n")
    text.write("f'Greatest Decrease in Profits: ${max_loss}'" + "\n")