import pandas as pd
file = open("Datasets/car.data","r")
dataset = pd.DataFrame(columns=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
for line in file.readlines():
    data = line;
    data = data.split(',')
    dataset = dataset.append({'buying': data[0], 'maint':data[1], 'doors':data[2], 'persons': data[3], 
                            'lug_boot': data[4], 'safety': data[5]}, ignore_index=True)
dataset.to_csv('car.csv', index=False)
    