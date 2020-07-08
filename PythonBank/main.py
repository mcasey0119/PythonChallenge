import os
import csv

#define path from which the file is
#'..' means going back up a folder - following path from there
csvpath = os.path.join('Resources', 'PythonBank_Resource.csv')

#define variables
total_months = []
net_profit = []
avg_change = []
greatest_profit = []
greatest_loss = []

with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    header = next(data)

   # counter = 0
    #for row in data:
       # counter = counter +1
       # print(counter) -- this is all assistance from tutoring
    
    #add the total months and net profit to the list associated with that variable
    for row in data:
        total_months.append(row[0])
        net_profit.append(int(row[1]))
    
    for i in range(len(net_profit)-1):
         avg_change.append(net_profit[i+1]-net_profit[i])        

    greatest_profit.append(max(avg_change))
    greatest_loss.append(min(avg_change))
        
    
    
print('Financial Analysis')
print('--------------------')
print(f"Total Months: {len(total_months)}")
print(f"Net Profit: ${sum(net_profit)}")
#average of the "profit/losses" column (adding them up and dividing by count)
print(f"Average Change Overall (sum of columns/count): ${sum(net_profit)/len(total_months)}")
print(f"Average Change: {round(sum(avg_change)/len(avg_change),2)}")
print(f"Greatest Profit: {max(avg_change)}")
print(f"Greatest Loss: {min(avg_change)}")

#output this file as a text file per homework instructions
output = os.path.join('Analysis', 'PyBank_TxtAnalysis.txt')


with open(output, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("-----------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Months: {len(total_months)}")
    txt_file.write("\n")
    txt_file.write(f"Net Profit: ${sum(net_profit)}")
    txt_file.write("\n")
    txt_file.write(f"Average Change Overall (sum of columns/count): ${sum(net_profit)/len(total_months)}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: {round(sum(avg_change)/len(avg_change),2)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Profit: {max(avg_change)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Loss: {min(avg_change)}")


