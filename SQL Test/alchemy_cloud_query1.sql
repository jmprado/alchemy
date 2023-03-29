use jprado_test;

select
    *
from
    employees
where
    reportsTo = (
        select
            employeeNumber
        from
            employees
        where
            lastName = 'Bow'
            and firstName = 'Anthony'
            and jobTitle like 'Sales Manager%'
    );