import pandas as pd 
daily_new_deaths_file = open('Daily-new-deaths.txt', 'r')
daily_new_cases_file = open('Daily-new-cases.txt', 'r')

string_file = daily_new_deaths_file.read()
Dict = {}
Dict = {'Date': string_file[string_file.find("Feb"):string_file.find("Apr 25")+6].split('","')}
Dict['Daily_new_deaths'] = string_file[string_file.find("data")+7:string_file.find("responsive")-22].split(",")

string_file = daily_new_cases_file.read()
Dict['Daily_new_cases'] = string_file[string_file.find("data")+7:string_file.find("responsive")-22].split(",")
Dict["Country"] = ['Moldova' for i in range(len(Dict['Date']))]
            
dataset = pd.DataFrame(data=Dict)
dataset.to_csv("Moldova_coronavirus_cases_data.csv", index=False)