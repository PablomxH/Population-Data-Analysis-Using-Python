import csv_reader

def filtro(selection,parameter):
    data=csv_reader.csv_reader()
    search=list(filter(lambda item:item[parameter]==selection,data))
    print(search[0])