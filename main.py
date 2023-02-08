import buscador

def run():
    try:
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
