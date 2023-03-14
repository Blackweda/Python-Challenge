import csv
import os

#filepath = "Resources/budget_data.csv"
filepath = os.path.join("Resources", "budget_data.csv")

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


with open(filepath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)    # Date, Profit/Losses

    for row in csvreader:

        # Every row add to the months
        months_count = months_count + 1

        # Every row add to the profit/loss amount
        profit_loss_total_amount = profit_loss_total_amount + int(row[1])

        # Track the changes in profit/loss and average the results
        if months_count == 1:
            profit_loss_changes.append(int(row[1]))
            print("first entry: " + row[1] + " and size of plc: " + str(len(profit_loss_changes)))
        else:    
            profit_loss_changes.append(int(row[1]) - profit_loss_changes[len(profit_loss_changes)-1])
            print("row1: " + row[1] + " minus: " + str((profit_loss_changes[len(profit_loss_changes)-1])) + " equals: " + str(int(row[1]) - profit_loss_changes[len(profit_loss_changes)-1]))
      
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
    print(f"Average Change: ${profit_loss_changes_average}\n") 
    print(f"Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit_amount})\n")
    print(f"Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss_amount})")

    # Write information to an Analysis folder
    analysis_file = os.path.join("Analysis", "budget_data_analysis.txt")
    
    with open(analysis_file, "w") as datafile:

        mc = repr(months_count)
        plta = repr(profit_loss_total_amount)
        plca = repr(profit_loss_changes_average)
        gpa = repr(greatest_profit_amount)
        gla = repr(greatest_loss_amount)
        
        analysis = "\
Financial Analysis\n\
------------------\n\
Total Months: " + mc + "\n\
Total: $" + plta + "\n\
Average Change: $" + plca + "\n\
Greatest Increase in Profits: " + greatest_profit_date + " $(" + gpa + ")\n\
Greatest Decrease in Profits: " + greatest_loss_date + " $(" + gla + ")"

        datafile.write(analysis)

        datafile.close