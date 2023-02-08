import filter
import csv_reader
import charts
import csv

def browser():
    menu=input("""
    Parameters:
    [1]Rank     [3]Capital
    [2]Country  [4]Continet
    
    What do you wanna search?: """)
    print(' ')

    try:   
        if int(menu)==1:
            selection=input("""    Introduce a rank: """)
            filter.filtro(selection,parameter='Rank')
        elif int(menu)==2:
            selection=input("""    Introduce a country: """)
            filter.filtro(selection,parameter='Country/Territory')
        elif int(menu)==3:
            selection=input("""    Introduce a capital: """)
            filter.filtro(selection,parameter= 'Capital')
        elif int(menu)==4:
            selection=input("""    Introduce a continent: """)
            filter.filter_for_Continent(selection,parameter='Continent')
        else:
            print('That is not an option')
    except IndexError:
        print('Invalid parameter')

def population():
    options=input("""
    Options of population:
    [1]Country    
    [2]Comparison between countries 
    
    What do you wanna watch?: """)

    if int(options)==1:
        print(' ')
        selection=input("""    Introduce a country: """)
        search=filter.filter_for_population(selection,parameter='Country/Territory')
        print(search[0])
        country_dict=search[0]
        labels,values=charts.get_population(country_dict)
        charts.generate_bar_chart(labels,values)
    elif int(options)==2:
        pass
    else:
        print('That is not an option')

    