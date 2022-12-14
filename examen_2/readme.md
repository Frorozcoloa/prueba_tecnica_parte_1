# Prueba Examen 2
Esta es el segundó examen de la prueba de bancolombia.

## directorio

```
1_crear_tablas.sql --> Código sql de las tablas propuestas
2_ingresar_valores.sql --> Los valores para llenar las tablas de sql
examen_python --> Explicación de los puntos de python
puntos.sql --> Querys para realizar los puntos en sql.
readme.md --> Explicación del proyecto
```

## Primer punto SQL
Todo fue hecho en sqlite
1. Está query se desarrolla por medio de ```GROUP BY```, se hace un ```JOIN``` para unir la tabla de ciudad con de usario.
2. Lo que se hace, es hacer un JOIN entre la tabla TRANSACTIONS y la tabla cities, luego, se saca el nombre, el mino de cant y max trx_total_amount
3. Para el tercer query, lo primero es hacer un subquery donde se saqué los valores tanto de In como Out. Con el Where se saca saca por mes y se hace la resta (Quedó debiendo el query)
4. Where se hace a cada registro, el having se hace un grupo de registro y siempre va despues de un Group By
   1. DROP, elimina la tabla, Truncate elimina todos los registros de la base de datos.
   2. UNION se utiliza para seleccionar los datos reacionando entre tablas pero devuelve los distintos, el UNION ALL devuelve todos los valore.
5. La función es IS NOT NULL
6. Los Triggers son procedimientos almacenados asociados a la manipulación de datos en una tabla específica. 
7. El problema que se puede ver es que col1 puede pertenecer tanto a table3 como tabla1

## Segundo Punto PYTHON
Revisar el examen_python.py