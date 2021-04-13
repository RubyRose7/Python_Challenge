import os
import csv 

#Define variables 
Total_Months= []
Dates= []
Net_Profit_Loss= []
Changes_Profit_Loss= []
Greatest_Increase_Profit= []
Greatest_Decrease_Loss= []

Budget_Path= os.path.join('Resources','budget_data.csv')
newpath= os.path.join('analysis', 'analysis.txt')

#Read CSV file
with open (Budget_Path) as csvfile:
	csvreader= csv.reader(csvfile, delimiter= ',')
	header= next (csvreader)

	
	# To find the total profit/loss
# Read through each row of data after header
	for rows in csvreader:
		Net_Profit_Loss.append(int(rows[1]))
		Total_Months.append(rows[0])

#To find the change in profit/loss
for x in range(1, len(Net_Profit_Loss)):
	Changes_Profit_Loss.append((int(Net_Profit_Loss[x])-int(Net_Profit_Loss[x-1])))


#To find Average in Changes of Profit/Loss
average= sum(Changes_Profit_Loss)/len(Changes_Profit_Loss)


# To find Greatest Increase in Profit 
Greatest_Increase_Profit= max(Changes_Profit_Loss)

# To find Greatest Decrease in Profit/Loss
Greatest_Decrease_Loss= min(Changes_Profit_Loss)


#To check length of total months
Months= len(Total_Months)


#To Print Results
with open (newpath, 'w') as textfile:
	print("Financial Analysis") 
	print(".........................")
	print("Total Months: " + str(Months))
	print("Total: " + "$" + str(sum(Net_Profit_Loss)))
	print(f"Average Change: ${round(average, 2)}")
	print(f"Greatest Increase in Profits: $({Greatest_Increase_Profit})")
	print(f"Greatest Decrease in Profits: $({Greatest_Decrease_Loss})")
	textfile.write("Financial Analysis\n")
	textfile.write(".........................\n")
	textfile.write(f"Total Months: {str(Months)}\n")
	textfile.write(f"Total: $ {str(sum(Net_Profit_Loss))}\n")
	textfile.write(f"Average Change: ${round(average, 2)}\n")
	textfile.write(f"Greatest Increase in Profits: $({Greatest_Increase_Profit})\n")
	textfile.write(f"Greatest Decrease in Profits: $({Greatest_Decrease_Loss})\n")

