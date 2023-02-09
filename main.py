import buscador

#I define the first interaction of the program
#according to the request redirect the user to different modules.

def run():
    try:                                        #Error handling in case of an invalid option.
        option=int(input("""
    Search by:
    [1] Population of a country by year
    [2] Rank,capital,country etc.
        
    Choose an option:   """))
    

        if option==1:
            buscador.population()
        elif option==2:
            buscador.browser()
        else:
            print('That is not an option')
    except ValueError:
        print('That is not an option')


if __name__=='__main__':
    run()
