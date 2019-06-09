# Cubic Matrix

#### **Instalación**
- Clonar el repositorio

`
$ git clone git@github.com:IvanBodnar/cubic_matrix.git
`

`
$ cd cubic_matrix
`

- Crear y activar un virtualenv con Python 3.6.8 +

`
$ python3.7 -m venv venv
`

`
$ source venv/bin/activate
`

- Instalar las dependencias externas (usa solo pytest)

`
$ pip install -r requirements.txt
`

#### Uso de la clase CubicMatrix
La clase se instancia pasando como parámetros la cantidad de  
columnas, cantidad de filas y cantidad de "páginas" (z index):

`
$ cm = CubicMatrix(3, 3, 4)
`

Luego, puede ejecutarse el método execute, pasando un string  
con el comando deseado:

`
$ cm.execute('UPDATE 1 1 1 10')
`

`
$ cm.execute('QUERY 1 1 1 3 3 1')
`

#### **Tests**
En el package tests se encuentran los tests unitarios para  
cada módulo, así como también **test_main.py**, en el cual  
se encuentran los tests que validan el comportamiento final  
esperado. Se pueden agregar tests creando métodos dentro de  
la clase TestMain, instanciando CubicMatrix y agregando asserts,  
usando como modelo los tests anteriores.
- Correr todos los tests

`
$ pytest
`

- Correr solamente test_main.py

`
$ pytest cubic_matrix/tests/test_main.py
`