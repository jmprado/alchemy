use jprado_test;

select
    p.*,
    o.*,
    od.priceEach
from
    products p
    inner join orderDetails od on p.productCode = od.productCode
    inner join orders o on o.orderNumber = od.orderNumber 
where
    od.priceEach between 100
    and 150;