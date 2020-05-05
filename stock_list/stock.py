import csv

csv_file = "/home/atamayo/Mission/SPRING2020/CIS008/FINAL/stock_list/companylist.csv"
ticker_list = list()

def retrieve_tix(u_answer,tick_list):
	if u_answer in tick_list:
		print("Found your tick mark")
	else:
		print("Did not find that TIX, please try again")
	return u_answer

def extract_ticker_symbols(u_file,tix_symbols):
	with open(u_file, newline='') as opencsv:
		reader = csv.reader(opencsv,quotechar='|')

		for row in reader:
			for items in row[0:1]:
				ticker_list.append(items)
		print("Successfully extracted data")
	return ticker_list


def main():
	quit_key = "done"
	extract_ticker_symbols(csv_file,ticker_list)
	while True:
		#Allowing the user to pass multiple stock letters
		user_stocks = list()
		stock_letters = input("Enter up to 4 letters to search for ticker stock " + \
								"Enter 'done' to quit : ")
		if stock_letters == quit_key:
			quit()
		try:
			if stock_letters.isalpha():
				print("is alpha")
				stock_letters = stock_letters.upper()
				stock_letters = '"' + stock_letters + '"'
				print(stock_letters)
				retrieve_tix(stock_letters,ticker_list)
		except ValueError as error:
			print('invalid input', error)

if __name__ == '__main__':
	main()