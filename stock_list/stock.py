import os.path
import sys
import csv
import re

'''This is the listing of ticker source files:
C:/Users/marma/Documents/Ex_Files_Trading_Finance_Python_R_Stata/Exercise Files/ch02/02_06/textfile_pharma.csv
textfile_pharma
textfile_ev
textfile_corp
textfile
'''
#csv_file = 'C:/Users/marma/Documents/PythonEzzat/CIS-Python/stock_list/companylist.csv'
# Prompt the user to enter filenames
csv_file = input("Enter a ticker names source file: ").strip()
# Check if source file exists
if os.path.isfile(csv_file):
	print(csv_file + " ticker file exists")

else:
	print("File is missing")
	sys.exit()


def retrieve_tix(u_answer,tick_list):
	if u_answer in tick_list:
		print("Found your tick mark")
	else:
		print("Did not find that TIX, please try again")
	return u_answer


def extract_ticker_symbols(u_file,tix_symbols):
	with open(u_file, newline='') as opencsv:
		reader = csv.reader(opencsv,quotechar=',')

		for row in reader:
			for items in row[0:1]:
				ticker_list.append(items)
		print("Successfully extracted data")
	return ticker_list


def main():

	while True:

		stock_letters = input("Enter up to 4 letters to search for ticker stock " + \
								"Enter 'done' to quit : ")
		quit_key = "done"
		if stock_letters == quit_key:
			quit()
		try:
			#if stock_letters.isalpha(): #Use 'rstrip' to allow only string characters
			if stock_letters.rstrip() and re.search('[0-9]+', stock_letters):
				print("is valid ticker")
				stock_letters = stock_letters.upper()
				#stock_letters = '"' + stock_letters + '"' #Remove string quotes, variable type is already string
				stock_letters = stock_letters
				print(stock_letters)
				retrieve_tix(stock_letters,ticker_list)
		except ValueError as error:
			print('invalid input', error)

if __name__ == '__main__':
	main()
