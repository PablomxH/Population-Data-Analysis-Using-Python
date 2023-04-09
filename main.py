import buscador
import tools

#I define the first interaction of the program
#according to the request redirect the user to different modules.

def run():
    print("Welcome to the World Population Finder")

    while True:
        try:                                        #Error handling in case of an invalid option.
            option=int(input("""
        Write a number search by:

        [1] Population of a country by year     Graphs
        [2] Rank,capital,country etc.

        [3] Exit ⌫
      
        Choose an option:   """))
        
            tools.clear_screen()
        
            if option==1:
                buscador.population()
            elif option==2:
                buscador.browser()
            elif option==3:
                print('Thank you for using the World Population Finder')
                break
            else:
                print('That is not an option, please select a valid option')


        except ValueError:
            print('That is not an option, please select a valid option')


if __name__=='__main__':
    run()
