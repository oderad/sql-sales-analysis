# Displays All Sales from Canada 
select 
s.sales,
c.country,
p.product
from 
pbi_practice.sales_fct s
join pbi_practice.country_dim c on c.coun_key = s.cty_key
join pbi_practice.prod_dim p on p.prod_key = s.prd_key
join pbi_practice.seg_dim g on g.seg_key = s.seg_key
where 
c.country in ('Canada')





