#!/usr/bin/env python
# coding: utf-8

# In[70]:


csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_headers = next(csvreader)

    month = 0 # number of months in csv
    net_profit = 0 # net profit over entire timeline
    profit_change = [] # list to track month-to-month change
    prev_profit = 0 # profit from previous month
    total_change = 0 # sum of change list
    max_change = 0 # greatest profit increase
    max_date = ""
    min_change = 0 # greatest profit decrease
    min_date = ""
    
    for x in csvreader:
        # keep track of how many months
        month = month + 1
        
        # find this month's profit and add to net
        profit = float(x[1])
        net_profit = net_profit + profit
        
        # find change from previous month and add to list
        change = profit - prev_profit
        profit_change.append(change)
        
        # find max/min change
        if change > max_change:
            max_date = x[0]
            max_change = change
        elif change < min_change:
            min_date = x[0]
            min_change = change
        
        # sum profit change
        total_change = total_change + change
        
        # update prev_profit before next iteration
        prev_profit = profit
    
        # print stuff
    print("Financial Analysis \n ----------------------------")
    print(f"Total Months: {month}")
    print(f"Total: {net_profit}")
    print(f"Average Change: {total_change/month}")
    print(f"Greatest Increase in Profits: {max_date} (${max_change}0)")
    print(f"Greatest Decrease in Profits: {min_date} (${min_change}0)")
        
        # create & write textfile
    csvoutput = os.path.join("analysis", "analysis.txt")
    
    with open(csvoutput,"a") as txtfile:
        txtfile.write(f"Total Months: {month}\n")
        txtfile.write(f"Total: {net_profit}\n")
        txtfile.write(f"Average Change: {total_change/month}\n")
        txtfile.write(f"Greatest Increase in Profits: {max_date} (${max_change}0)\n")
        txtfile.write(f"Greatest Decrease in Profits: {min_date} (${min_change}0)\n")


# In[ ]:




