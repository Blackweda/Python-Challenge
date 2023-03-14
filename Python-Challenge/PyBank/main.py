import csv

filepath = "Resources/budget_data.csv"

with open(filepath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    months_count = 0

    profit_loss_total_amount = 0

    profit_loss_changes = []
    profit_loss_changes_average = 0
    
    # Tracking the greatest profit
    greatest_profit_amount = 0
    greatest_profit_date = ""

    # Tracking the greatest loss
    greatest_loss_amount = 0
    greatest_loss_date = ""

    for row in csvreader:

        # Every row add to the months
        months_count = months_count + 1

        # Every row add to the profit/loss amount
        profit_loss_total_amount = profit_loss_total_amount + int(row[1])

        # Track the changes in profit/loss and average the results
        if months_count == 1:
            profit_loss_changes.append(int(row[1]))
        else:    
            profit_loss_changes.append(int(row[1]) - profit_loss_changes[len(profit_loss_changes)-1])
      
        # Determine if this row is the greatest profit (so far)
        if int(row[1]) > greatest_profit_amount:
            greatest_profit_amount = int(row[1])
            greatest_profit_date = row[0]

        # Determine if this row is the greatest loss (so far)
        if int(row[1]) < greatest_loss_amount:
            greatest_loss_amount = int(row[1])
            greatest_loss_date = row[0]

    # Grab the average of the total profits/losses
    for i in profit_loss_changes:

        profit_loss_changes_average += i

    profit_loss_changes_average / len(profit_loss_changes)
    
    print("Financial Analysis\n")
    print("------------------\n")

    
    print(f"Total Months: {months_count}\n")
    print(f"Total: ${profit_loss_total_amount}\n")   
    print(f"Average Change: (${profit_loss_changes_average})") 
    print(f"Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit_amount})\n")
    print(f"Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss_amount})")
    



    






