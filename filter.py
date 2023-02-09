import csv_reader
import charts

def filtro(selection,parameter):
    data=csv_reader.csv_reader()
    search=list(filter(lambda item:item[parameter]==selection,data))
    print(search[0])
    return search

def filter_for_Continent(selection,parameter):
    data=csv_reader.csv_reader()
    search=list(filter(lambda item:item[parameter]==selection,data))
    print(search)

def filter_for_population(selection,parameter):
    data=csv_reader.csv_reader()
    search=list(filter(lambda item:item[parameter]==selection,data))
    return search

def comparsion():
    print('')
    continent=input('    Write a continent: ')
    data=csv_reader.csv_reader_filter(continent)
    if len(data)>0:
        countries=list(map(lambda x:x['Country/Territory'], data))
        per=list(map(lambda x:x['World Population Percentage'], data))
        charts.generate_pie_chart(countries,per)
    else:
        print('Thats not an option')

def population_country():
    print(' ')
    selection=input("""    Introduce a country: """)
    search=filter_for_population(selection,parameter='Country/Territory')
    print(search[0])
    country_dict=search[0]
    labels,values=charts.get_population(country_dict)
    charts.generate_bar_chart(labels,values,selection)

def two_countries():
    print(' ')
    selection=input("""    Introduce a country: """)
    search=filter_for_population(selection,parameter='Country/Territory')
    country_dict=search[0]
    values=charts.get_population(country_dict)
    #print(values[1])

    print(' ')
    selection2=input("""    Introduce a country: """)
    search2=filter_for_population(selection2,parameter='Country/Territory')
    country_dict2=search2[0]
    values2=charts.get_population(country_dict2)
    #print(values2[1])

    charts.two_charts(values[1],values2[1],selection,selection2)

