# Displays All Sales from Canada ordered by Sales in descending order, asc for ascending order and desc for descending order, if none specified by default then it will display in ascending order
select 
s.sales,
c.country,
p.product,
s.date
from 
pbi_practice.sales_fct s
join pbi_practice.country_dim c on c.coun_key = s.cty_key
join pbi_practice.prod_dim p on p.prod_key = s.prd_key
join pbi_practice.seg_dim g on g.seg_key = s.seg_key
where 
c.country in ('Canada')
order by s.sales desc





