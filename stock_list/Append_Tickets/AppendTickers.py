#get_data_for_multiple_stocks
raw = ['NEM','FDVV','TLT','SAGE','IEFA','GOLD','FCNTX','JGH','AAXJ','FREL','SINA','WRB','SNP','CHL','CMA','VLO','SANM','SLVP','HDV','T']
# should already be initialized
raw.sort()

while True:
    #number = 0.0
    input_letters = input('Enter up to 4 letters to search for ticker stock.  Enter "done" to quit: ')
    if input_letters == 'done':
        quit()
    try:
        check = input_letters.isalpha()
        print(check)
        input_letters = input_letters.upper()
        lett_len = len(input_letters)
        if check is False:
            print('Invalid input0')
            continue
        elif lett_len < 0 or lett_len > 4:
            print('Invalid input1')
            continue
        #elif lett_len < 0 and lett_len < 5:
            #quit()

    except ValueError as e:
        print(e)
        print('Invalid input2')
        quit()

    raw.append(input_letters)
    raw.sort()
    print(raw)
