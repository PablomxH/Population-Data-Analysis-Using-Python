import buscador
import filter
import csv
import csv_reader

def run():
    option=int(input("""
    Search by:
    [1] Population by year
    [2] Rank,capital, country etc.
    
    Choose an option:   """))
    
    if option==1:
        buscador.population()
    elif option:
        buscador.browser()


if __name__=='__main__':
    run()
