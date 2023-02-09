import matplotlib.pyplot as plt

#function to extract only population from the dictionary
def get_population(country_dict):
    population_dict={
        '2022':int(country_dict['2022 Population']),
        '2020':int(country_dict['2020 Population']),
        '2015':int(country_dict['2015 Population']),
        '2010':int(country_dict['2010 Population']),
        '2000':int(country_dict['2000 Population']),
        '1990':int(country_dict['1990 Population']),
        '1980':int(country_dict['1980 Population']),
        '1970':int(country_dict['1970 Population']),
    }
    labels=list(population_dict.keys())
    values=list(population_dict.values())
    return labels, values

#graph for population of a country
def generate_bar_chart(labels,values,country):
    fig, ax = plt.subplots()
    ax.plot(labels, values)
    ax.set_xlabel('Years')
    ax.set_ylabel('Population')
    ax.set_title('Population of '+country)

    plt.show()

#pie chart
def generate_pie_chart(labels,values):
    fig, ax=plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show()

#graph for population of 2 countries
def two_charts(country1,country2,name1,name2):
    #x = [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022]
    x = [2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970]
    y1 = country1
    y2 = country2

    fig, ax = plt.subplots()

    ax.plot(x, y1, label=name1)
    ax.plot(x, y2, label=name2)

    ax.set_xlabel('Years')
    ax.set_ylabel('Population')
    ax.set_title('Comparison between countries')
    ax.legend()

    plt.show()