#Run this file inside the git repository git repro final python
import os
import csv

#extracted and cleaned ticker list
csv_ticker_list= list()
#user current dir
cwd = os.getcwd()
#new company csv to read off of
new_u_file = "complete_ticker_list.csv"
#complete path file
abs_file_path = os.path.join(cwd,new_u_file)

def return_tickers_from_csv(ticker_list,tick_csv_file):
	with open(tick_csv_file, newline='') as opencsv:
		reader = csv.reader(opencsv,quotechar=',')
		for row in reader:
			for items in row[0:1]:
				ticker_list.append(items)
	print('Successfully created list')
	return ticker_list


#MULTIPLE TICK SUPPORT
def return_multiple_tix(user_ticker_list,csv_tick_list,valid_options):
	#This function returns the valid tick options after checking the complete_ticker_list.csv
	for ticks in user_ticker_list:
		if ticks in csv_tick_list:
			print(ticks, " is valid appending to list")
			valid_options.append(ticks)
		else:
			print("{} is NOT a valid ticker ".format(ticks))
	#print("Valid options were ", valid_options)
	return valid_options

def main():
	return_tickers_from_csv(csv_ticker_list,abs_file_path)
	# print(csv_ticker_list)
	#this list is used  append  multiple user tickers, it checks if the ticks are valid by seeing if
	#they exist in csv_ticker_list, if the tick is valid it appends to a valid list,
	user_ticks = list()
	quit_key = ('done')
	valid_options = list()
	while True:
		#Allowing the user to pass multiple stock letters
		tick_letters = input("Enter multiple ticks to search for valid ticker marks " + \
								"Enter 'done' to quit : ")
		multiple_ticks_list = tick_letters.split(",")
		if tick_letters == quit_key:
			break
		if len(multiple_ticks_list) == 1:
			print("only added one key")
			break		
		if len(multiple_ticks_list) > 1:
			for tick in multiple_ticks_list:
				user_ticks.append(tick)
	return_multiple_tix(user_ticks,csv_ticker_list,valid_options)
	print(valid_options)

if __name__ == '__main__':
	main()