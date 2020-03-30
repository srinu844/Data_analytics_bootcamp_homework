import csv

# Files to load (Remember to change these)
file_to_load = "../PyBank/Resources/budget_data.csv"
output_file = "../PyBank/budget_analysis.txt"


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)

    # use of next to skip first title row in csv file
    next(reader) 
    Profit_Losses = []
    date = []
    avg_change = []
    date_final = []
    total_sum = []

    # in this loop I did sum of column 1 which is Profit/Losses in csv file and counted total months which is column 0 
    for row in reader:

        Profit_Losses.append(float(row[1]))
        date.append(row[0])

    date_final = len(date)
    total_sum = sum(Profit_Losses)

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", date_final)
    print("Total : $", total_sum)


    #in this loop I did total of difference between all row of column "Profit/Losses" and found average change. Also found out greatest increase in change and greastesr decrease in change. 
    for i in range(1,len(Profit_Losses)):
        avg_change.append(Profit_Losses[i] - Profit_Losses[i-1])   
        avg_diff_change = sum(avg_change)/len(avg_change)

        max_change = max(avg_change)

        min_change = min(avg_change)

        max_change_date = str(date[avg_change.index(max(avg_change))+ 1])
        min_change_date = str(date[avg_change.index(min(avg_change))+ 1])


    print("Avereage Change: $", round(avg_diff_change, 2))
    print("Greatest Increase in Revenue:", max_change_date,"($", max_change,")")
    print("Greatest Decrease in Revenue:", min_change_date,"($", min_change,")")


with open(output_file, 'w') as txt_file: 

    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months:" + str(date_final))
    txt_file.write("\n")
    txt_file.write("Total : $" + str(total_sum))
    txt_file.write("\n")
    txt_file.write("Avereage Change: $" + str(avg_diff_change))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Revenue:" + str(max_change_date) + " ($" + str(max_change)+ ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Revenue:" + str(min_change_date) + " ($" + str(min_change)+ ")")


