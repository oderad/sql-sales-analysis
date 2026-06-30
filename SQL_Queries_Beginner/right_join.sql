# Displays all sales and all data utilizing right joins
# A right join brings everything from the right table and everything matching in the left table
select 
*
from 
pbi_practice.sales_fct s
right join pbi_practice.country_dim c on c.coun_key = s.cty_key
right join pbi_practice.prod_dim p on p.prod_key = s.prd_key
right join pbi_practice.seg_dim g on g.seg_key = s.seg_key






