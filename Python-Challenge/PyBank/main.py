import csv
import os

#filepath = "Resources/budget_data.csv"
filepath = os.path.join("Resources", "budget_data.csv")

months_count = 0

profit_loss_total_amount = 0

# Tracking month-to-month changes
profit_loss_figures = []
month_difference = 0
profit_loss_figures_differences = []
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

        # Keep record of this month's figures
        profit_loss_figures.append(int(row[1]))
                
        # Track the changes in profit/loss and average the results
        if months_count > 1:    # if this is 2nd month moving forward (so profit_loss_figures size is greater than 1)
            month_difference = profit_loss_figures[len(profit_loss_figures)-1] - profit_loss_figures[len(profit_loss_figures)-2]

        # on the first row, both month_difference and greatest_profit(loss)_amount will be zero... therefore everything will adjust consequently
        if month_difference > greatest_profit_amount:
            greatest_profit_amount = month_difference
            greatest_profit_date = row[0]

        if month_difference < greatest_loss_amount:
            greatest_loss_amount = month_difference
            greatest_loss_date = row[0]

        if months_count > 1:        # I don't want to have the initialization value of 0 skewing the averages
            profit_loss_figures_differences.append(month_difference)    # keep track of the differences between months      
         

    # Grab the average of the total profits/losses
    for i in profit_loss_figures_differences:

        profit_loss_changes_average += i

    profit_loss_changes_average = profit_loss_changes_average / len(profit_loss_figures_differences)
    
    print("Financial Analysis\n")
    print("------------------\n")    
    print(f"Total Months: {months_count}\n")
    print(f"Total: ${profit_loss_total_amount}\n")   
    print(f"Average Change: ${round(profit_loss_changes_average, 2)}\n") 
    print(f"Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit_amount})\n")
    print(f"Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss_amount})")

    # Write information to an Analysis folder
    analysis_file = os.path.join("Analysis", "budget_data_analysis.txt")
    
    with open(analysis_file, "w") as datafile:

        mc = repr(months_count)
        plta = repr(profit_loss_total_amount)
        plca = repr(round(profit_loss_changes_average, 2))
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