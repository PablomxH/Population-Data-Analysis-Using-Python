# Population Python_CSV-Matplotlib :fa-bar-chart:

![]](https://img.shields.io/github/tag/pandao/editor.md.svg) 

Extracción de datos de un CSV, filtros de datos, transformación y generación de gráficos con Matplotlib, el programa se subdivide en diferentes módulos para segmentar el código.

###CSV:
[World Population Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset "World Population Dataset")

**Contenido:**

[TOCM]

[TOC]
## main.py
Módulo principal que secciona el programa de acuerdo a las peticiones del usuario, e importa el modulo de buscador que hará la petición.

```python
option=int(input("""
	Write a number search by:

    [1] Population of a country by year
    [2] Rank,capital,country etc.
        
    Choose an option:   """))
    

	if option==1:
		buscador.population()
	elif option==2:
		buscador.browser()
```

## buscador.py
Modulo encargado de llamar a los filtros necesarios de acuerdo a la peticion del usuario.

## charts.py
Módulo para la generación de gráficos.

```python
def generate_bar_chart(labels,values,country):
    fig, ax = plt.subplots()
    ax.plot(labels, values)
    ax.set_xlabel('Years')
    ax.set_ylabel('Population')
    ax.set_title('Population of '+country)

    plt.show()
```

## csv_reader.py
Lectura del origen de datos, CSV del [World Population Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset "World Population Dataset")
```python
def csv_reader():
    with open('./population.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data=[]       
        for row in reader:
            iterable =zip(header,row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
        return data
```

## filter.py
Módulo de las distintas funciones de filtros del CSV para las peticiones del usuario.
```python
def population_country():
    print(' ')
    selection=input("""    Introduce a country: """)
    search=filter_for_population(selection,parameter='Country/Territory')
    print(search[0])
    country_dict=search[0]
    labels,values=charts.get_population(country_dict)
    charts.generate_bar_chart(labels,values,selection)
```

##Acerca del proyecto...
...