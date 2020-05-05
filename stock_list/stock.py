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
	extract_ticker_symbols(csv_file,ticker_list)
	user_tix = input("Please enter a valid ticker from Nasdaq: ")
	user_tix = '"' + user_tix + '"'
	retrieve_tix(user_tix,ticker_list)



if __name__ == '__main__':
	main()