insert into CITIES values 
(1, "Medellín"),
(2, "Bogotá"),
(3, "Cali");

insert into clients values
(223122, 1, "Darío Ramirez",  3),
(445687, 1, "Sara Martinez", 2),
(112314, 3, "Darío Ramirez", 1),
(223141, 2, "Camilo Rios",   2),
(115662, 3, "Jose Carretero",1);

insert into  TRANSACTIONS values 
(1, 223122, 1, 20201002, 1500000, "In", 14, 1),
(2, 445687, 1, 20201014, 5354254, "In", 2, 1),
(3, 223122, 1, 20200912, 17250000, "Out", 4, 1),
(4, 223122, 1, 20200912, 110000000, "In", 8, 2),
(5, 445687, 1, 20201011, 50000, "In", 7, 3),
(6, 445687, 1, 20201011, 650000, "Out", 4, 2),
(7, 223141, 2, 20200825, 1200000, "Out", 1, 2),
(8, 223141, 2, 20200912, 235000, "Out", 2, 2),
(9, 223122, 1, 20200912, 45000, "In", 3, 3),
(10,112314,3,20200829,850000,"In",8,2),
(11, 115662, 3, 20200912, 1000000, "In", 7, 3);




SELECT trx_customer_id, SUM(trx_total_amount) as Total_in, substr(trx_date, 5,2) as month, trx_type  FROM transactions GROUP BY month, trx_type,trx_customer_id;
