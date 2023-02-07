import filter
import csv_reader
import csv

def browser():
    menu=input("""
    Parameters:
    [1]Rank     [3]Capital
    [2]Country  [4]Continet
    
    What do you wanna search?:""")
    
    if int(menu)==1:
        selection=input('Introduce a rank: ')
        filter.filtro(selection,parameter='Rank')
    elif int(menu)==2:
        selection=input('Introduce a country: ')
        filter.filtro(selection,parameter='Country/Territory')
    elif int(menu)==3:
        selection=input('Introduce a capital: ')
        filter.filtro(selection,parameter= 'Capital')
    elif int(menu)==4:
        selection=input('Introduce a continent: ')
        filter.filtro(selection,parameter='Continent')
    else:
        print('Search not found')

def population():
    pass
