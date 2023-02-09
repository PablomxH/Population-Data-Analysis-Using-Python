import csv_reader
import charts

#Here,filter all the information according to the request

#"filtro", receives from "browser" the parameter range, name etc, and the value of the parameter to filter
def filtro(selection,parameter):
    data=csv_reader.csv_reader()
    search=list(filter(lambda item:item[parameter]==selection,data))
    print(search[0])    #to view in dictionary format and not view a list with just a dictionary
    return search

#similar to "filtro" avoiding seeing only the first index
def filter_for_Continent(selection,parameter):
    data=csv_reader.csv_reader()
    search=list(filter(lambda item:item[parameter]==selection,data))
    print(search)

#Extraction of the entire population of a country
def filter_for_population(selection,parameter):
    data=csv_reader.csv_reader()
    search=list(filter(lambda item:item[parameter]==selection,data))
    return search

#comparison of population of a continent with pie chart
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

#graph of population growth of a country
def population_country():
    print(' ')
    selection=input("""    Introduce a country: """)
    search=filter_for_population(selection,parameter='Country/Territory')
    print(search[0])
    country_dict=search[0]
    labels,values=charts.get_population(country_dict)
    charts.generate_bar_chart(labels,values,selection)

#comparison graph of population growth of 2 countries
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

