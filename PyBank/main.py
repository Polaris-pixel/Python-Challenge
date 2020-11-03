import os
import csv

file_path = os.path.join ("Resources", "budget_data.csv")

with open (file_path, 'r') as storagefile:
    bank_reader = csv.reader (storagefile, delimiter=',')
    
    list_header = next(bank_reader)
    #print (f"Data Header: {list_header}")

    profit = 0
    months = 0
    months_list =[]
    count_row = 0
    initial_value = 0
    change_list = []
    for row in bank_reader:
        #print(row)
        change = int(row[1])- int(initial_value)
        change_list.append(change)
        initial_value = row[1]
        profit= profit + int(row[1])
        
        count_row += 1
        
        months += 1
        months_list.append(row[0])                   
        
        
avg_profit = profit/count_row 


# change is (2nd month - 1st month) and so on. 1st month is skipped
change_list.pop(0)

avg_change = sum (change_list)/len(change_list)

greatest_profit = max(change_list)

least_profit = min(change_list)

# +1 to take into account (index match) the 1st month skipped in line35
month_greatest_index= change_list.index(max(change_list))+1

month_least_index = change_list.index(min(change_list))+1

greatest_month = months_list[month_greatest_index]

least_month = months_list[month_least_index]

print ("Financial Analysis")
print ("------------------------")
print (f"Total Months : {months}")
print (f"Total = ${profit:0,.0f}")
print (f"Average Change: ${avg_change:0,.2f}")
print (f"Greatest Increase in Profits: {greatest_month} (${greatest_profit:0,.0f})")
print (f"Greatest Decrease in Profits: {least_month} (${least_profit:0,.0f})")


output_path = os.path.join("Analysis", "Summary_PyBank.txt")


with open(output_path, 'w') as bankfile: 
      
    bankfile.write('Financial Analysis \n')    
    bankfile.write('------------------------- \n')
    bankfile.write(f"Total Months :  {months} \n" )
    bankfile.write(f"Total =  ${profit:0,.0f} \n")
    bankfile.write(f"Average Change:  ${avg_change:0,.2f} \n")
    bankfile.write(f"Greatest Increase in Profits:  {greatest_month} (${greatest_profit:0,.0f}) \n")
    bankfile.write(f"Greatest Decrease in Profits:  {least_month} (${least_profit:0,.0f}) \n")

        


    