


#MULTIPLE TICK SUPPORT
def multiple_tix(m_stockList,tick_list):
	valid_options = list()
	for ticks in m_stockList:
		if ticks in tick_list:
			valid_options.append(ticks)
		else:
			print("Was not able to find {} ".format(ticks))
	print("Valid options were ", valid_options)

def main():
	#user_stocks = list()
	while True:
		#Allowing the user to pass multiple stock letters
		# stock_letters = input("Enter multiple ticks to search for ticker stock " + \
		# 						"Enter 'done' to quit : ")
		# multiple_stocks = stock_letters.split(",")
		# for tick in multiple_stocks:
		# 	user_stocks.append(tick)
		# if multiple_stocks > 1:
		# 	multiple_stocks(user_stocks,ticker_list)
if __name__ == '__main__':
	main()