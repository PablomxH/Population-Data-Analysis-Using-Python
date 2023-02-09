import csv
#reading from the database

#filter for most searches the information is extracted in a list of dictionaries
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

#filter for continents
def csv_reader_filter(continent):
    with open('./population.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data=[]
        
        for row in reader:
            iterable =zip(header,row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
        data_filter=list(filter(lambda i:i['Continent']==continent,data))
        return data_filter
