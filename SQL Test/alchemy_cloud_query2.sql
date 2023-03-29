use jprado_test;

select
    c.*, o.*
from
    customers c
    inner join orders o on c.customerNumber = o.customerNumber
where
    MONTH(o.shippedDate) = 8
    and YEAR(o.shippedDate) = 2003