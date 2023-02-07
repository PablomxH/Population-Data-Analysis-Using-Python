import csv

def csv_reader():
    with open('./population.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data=[]
        
        for row in reader:
            iterable =zip(header,row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
        return data