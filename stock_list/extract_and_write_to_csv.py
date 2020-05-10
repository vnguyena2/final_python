import os
import csv

#extracted and cleaned ticker list
ticker_list, clean_ticker_list = list() , list()

#comple nasdaq company list
ufile = "/home/atamayo/example_git/final_python/stock_list/companylist.csv"
#user current dir
cwd = os.getcwd()
#new company csv to read off of
new_u_file = "complete_ticker_list.csv"
#complete path file
abs_file_path = os.path.join(cwd,new_u_file)

def extract_ticker_symbols(u_file,ext_tix_symbols,clean_ticker_list):
	with open(u_file, newline='') as opencsv:
		reader = csv.reader(opencsv,quotechar=',')
		for row in reader:
			for items in row[0:1]:
				ext_tix_symbols.append(items)
		print("Successfully extracted data")
	for tix in ext_tix_symbols:
		tix = tix.replace('"','')
		clean_ticker_list.append(tix)
	print('Removed extra quotes')
	return clean_ticker_list


def create_csv_file(new_complete_csv_file,abs_path):
	#checkin if csv exists, if not create one!, else we break
	for r,d,f in os.walk(cwd):
		if not os.path.isfile(abs_file_path):
			print('file not found, creating new one in current directory named\n \
				complete_ticker_list.csv')
			fp = open(abs_path,'w+')
			fp.close()
			print("created_new_csv file")
			break
		else:
			print('found existing file')
			break

def write_to_csv(abs_path,cleaned_tix_symbols):
	cleaned_tix_symbols.sort()
	with open(abs_path, 'w+') as csvfile:
		fieldnames = ['TIX_symbols']
		writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
		writer.writeheader()

		for tix in cleaned_tix_symbols:
			writer.writerow({'TIX_symbols': tix})
	print('Successfully wrote tix to new csv file')


def main():
	create_csv_file(new_u_file,abs_file_path)
	extract_ticker_symbols(ufile,ticker_list,clean_ticker_list)
	write_to_csv(abs_file_path,clean_ticker_list)


if __name__ == '__main__':
	main()