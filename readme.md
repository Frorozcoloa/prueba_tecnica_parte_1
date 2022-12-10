# Prueba Técnica de Bancolombia. (Parte 1)

Está prueba, fue realizada con python 3.10.6.
Aquí hay dos formas de ejecutarse, una sería por medio de ```docker``` y la otra es que se instale el ```Ambiente virtual```.  Se le recomienda al usario hacerlo por medio de docker para no tener problemas con la versiones de python.

## Ambiente virtual.

* Compilaremos las librerías para que se adaté a la versión de python.
    ```
    pip-compile requierements.in
    ```
* Se genera el archivo con los requierements.txt, vamos a instalarlo.
    ```
    pip install -r requierements.txt
    ```
* Ejecutamos el archivo de python.(En algunos equipos se tienen dos versiones de python ```python``` la versión 2 y  ```python3``` la versión 3 )
* En la sentencia de python es con la versión 3
  ```
  python main.py
  ```

## Docker
* Creamos la imagen de docker
    ```
    docker image build -t banco:v1  . 
    ```
* Ejecutamos el archivo main.
* En windos la sentecía ```"$(pwd)"``` se cambia por ```cd```
* Importante que el docker esté compartiendo el volumen con el directorio actual de trabajo.
  ```
  docker run -it --rm -v "$(pwd)":/app banco:v1 python main.py
  ```

## Estructura del directorio.
```
data -> Archivos.csv donde se va a guardar los datos.
Dockerfile -> Intrucciones para crear la imagen
main.py --> Es donde se ejecuta todo.
Master.xlsx --> Es el output del programa
readme.md --> Explicación del proyecto.
requierements.in --> Nombre de las librerías a usar
```

## Explicación de la prueba

### Primer punto

  1. Todo fue realizado en linux  
  2. Se crea el ambiente virtual, creando el archivo requierements.in, y con el comando ```pip-compile``` se configura todo el proyecto, para configurar las dependecias y tambien las versiones (Pueden cambiar de linux a windows).
  3. Se crea un Dockerfile para hacer no tener problemas con versionamientos y el despligue se haga más rápido.

### Segundo punto

  1. La base de datos, se crea con la librería ```sqlite3```
  2. Se creó un archivo ```create_tables.sql```, donde está en código sql, la creación de la base de datos. Estó se hace con el fin de crear las relaciones entre las base de datos, pero no es necesario, ya que la librería pandas lo puede crear las tablas.
  3. El código lee todos los archivos que están dentro el directorio ```data```. Estós archivos son leidos con pandas y luego son guardados, en las respectivas tablas. En el momento se usan los nombres de los archivos para guardar en la base de datos (Lo ideal sería manejar un estandar para no crear tablas duplicadas).
  4. Se retonar todos los dataframes, y luego son guardados dentro de un diccionario, con la finalidad de usarse para crear la tabla Master
  5. La tabla Master, se crea, con una clave forena a la tabla transacciones (No se hace de manera explicita). Se traen todos los datos de la tabla User y se haceuna query para saber que valores están en la tabla Alerts.

### Tercer punto
    
1. Para rellenar los registro de las table master, lo que hacemos es hacer un merger outer (Todos los valores) entre los dataframes user y trx. 
2. Luego se hace un filtro, que devuelve un binario, donde por medio se pregunta que id de las transaciones está en el dataframe de alerts, y se le pone el nombre de ```is_claim``` 
3. Todo estó se guarda en datarame que luego, por el método ```to_sql``` se guarda en  ```sqlite```. 
4. Con el método ```to_excel```se guarda en un archivo de excel.

### Cuarto punto

La prueba fue realizada en linux y aunque es un requisito hacer el análisis en excel. Este lo voy en python.

1. Ideación en Miro
2. Análisis exploratorio
3. Modelo propuesto
4. Ideas

## Conclusioness