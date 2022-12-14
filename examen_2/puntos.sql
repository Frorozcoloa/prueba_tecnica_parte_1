-- 1. Realizar un Query para identificar la cantidad de clientes que hay por Ciudad.

SELECT cities.name, COUNT(*) 
FROM clients
INNER JOIN cities ON cities.id_city = clients.id_city
GROUP BY clients.id_city;

/*OUT
cities.name COUNT(*)
Medellín|2
Bogotá|2
Cali|1

*/

-- 2. Realizar un Query para identificar la ciudad con mayor monto transado de ingreso (In) "y" con el menor número de transacciones (cant) (de forma histórica, no importa la fecha de transacción).


SELECT cities.name, MIN(cant), MAX(trx_total_amount) 
FROM TRANSACTIONS
INNER JOIN cities ON cities.id_city = city
WHERE trx_type='In';

/* OUT
Bogotá|2|110000000
*/

-- Realizar un Query para identificar los clientes que, para el mismo mes, según su registro de transacciones cerró de forma negativa, es decir, que su monto transado de salida (Out) es mayor a los ingresos (In).

-- Para este punto, debemos de hacer dos querys
Select trx_customer_id from transactions
Group by trx_customer_id
Having sum(Select trx_total_amount from transactions where trx_type == "In") < sum(Select trx_total_amount from transactions where trx_type == "Out")






