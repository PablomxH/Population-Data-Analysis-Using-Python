import filter
import main
import tools

#browser, to choose according to which parameter we want to search for countries
#import filter since after selecting the parameter with filter we look for
#the required information
def browser():                          
    menu=input("""
    Parameters:
    [1]Rank     [3]Capital
    [2]Country  [4]Continet

    [5]Back
    
    What do you wanna search?: """)
    print(' ')

    try:
        tools.clear_screen()

        if int(menu)==1:
            selection=int(input("""    Introduce a rank: """))
            filter.filtro(selection,parameter='Rank')
        elif int(menu)==2:
            selection=input("""    Introduce a country: """)
            filter.filtro(selection,parameter='Country/Territory')
        elif int(menu)==3:
            selection=input("""    Introduce a capital: """)
            filter.filtro(selection,parameter= 'Capital')
        elif int(menu)==4:
            selection=input("""    Introduce a continent: """)
            filter.filtro(selection,parameter='Continent')
        elif int(menu)==5:
            main.run()
        else:
            print('That is not an option')
    except IndexError:
        print('Invalid parameter')


#population, to see the population, be it from a single country, comparison of 2 or from a continent
def population():
    options=input("""
    Options of population:
    [1]Country    
    [2]Comparison between countries

    [5]Back
  
    What do you wanna watch?: """)

    try:
        tools.clear_screen()
        
        if int(options)==1:
            filter.population_country()
        elif int(options)==2:
            option=input("""
    Options of population:
    [1]Comparison between two countries    
    [2]Comparison by continents
    
    [5]Back
    
    What do you wanna watch?: """)
            if int(option)==1:
                filter.two_countries()
            elif int(option)==2:
                filter.comparsion()
            elif int(option)==5:
                population()
            else:
                print('Thats not an option')
        elif int(options)==5:
            main.run()        
        else:
            print('That is not an option')
    except IndexError:
        print('Typing error, check the name')
    except ValueError:
        print('Invalid parameter')

