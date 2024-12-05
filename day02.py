input_file = 'day02-file-input.txt'

with open(input_file) as f:
    lines = f.readlines()

count = 0
safe_report = { 'safe' : 0, 'unSafe' : 0 }

for report in lines:
    state = "und"
    report.strip()
    levels_list = report.split()
    print(f'======={(count)}========')
    print(report)

    # if count == 20:
    #     exit()
    
    rate_store = { 'inc': 0,'dec': 0, 'eq': 0, 'delta' : 0 }

    for level in range(0,len(levels_list) - 1):
        print(f'comparing {levels_list[level]} to {levels_list[level + 1]}')
        # print(type(levels_list[level]))
        my_current = int(levels_list[level])
        my_next = int(levels_list[level + 1])

        if len(levels_list) < 2:
            print("List is too short to compare...exiting")
            exit()
        
        if my_current == my_next:
            rate_store['eq']+=1
        
        if my_current < my_next:
            print("increment!!!")
            rate_store['inc']+=1
        
        if my_current > my_next:
            print("decrement!!!")
            rate_store['dec']+=1
        
        delta = abs(int(levels_list[level]) - int(levels_list[level + 1]))
        print(f'delta: {delta}')
        if delta >= 1 and delta < 4:
            rate_store['delta'] = 0
        else:
            rate_store['delta'] = 1

        # print(rate_store)
        if rate_store['inc'] >= 1 and rate_store['dec'] >= 1:
            print("unSafe")
            safe_report['unSafe']+=1
            break
        
        # if rate_store['inc'] >= 1 and rate_store['dec'] == 0 or rate_store['inc'] == 0 and rate_store['dec'] >= 1:
        #     safe_report['safe']+=1

        if rate_store['eq'] >= 1:
            print("unSafe")
            safe_report['unSafe']+=1
            break

        if rate_store['delta'] >= 1:
            print('unSafe')
            safe_report['unSafe']+=1
            break

        print(rate_store)
   
    count+=1
    print(safe_report)
    print(len(lines))
    print("TOTAL SAFE REPORTS: ", len(lines) - safe_report['unSafe'])
    # print(state)
    # print(rate_store)