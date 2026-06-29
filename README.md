# SQL Sales Analysis Portfolio

## Overview

This repository demonstrates SQL concepts using the Microsoft Power BI Financial Sample dataset imported into MySQL.

Instead of using small toy examples, every query answers a realistic business question such as:

- Which country generated the highest sales?
- Which product has the highest profit?
- Which segment performs best?
- Which products are consistently top sellers?
- How do yearly sales compare?

The goal is to demonstrate SQL proficiency from beginner to advanced topics.

---

# Dataset

The dataset contains sales information with columns similar to:

| Column | Description |
|---------|-------------|
| Country | Country where sales occurred |
| Segment | Customer segment |
| Product | Product sold |
| Sales | Total sales amount |
| Profit | Profit generated |
| Units Sold | Number of units |
| Discount Band | Discount category |
| Year | Fiscal year |
| Month | Month of sale |

---

# SQL Topics Covered

| Topic | Difficulty |
|---------|------------|
| SELECT | Beginner |
| WHERE | Beginner |
| ORDER BY | Beginner |
| GROUP BY | Beginner |
| HAVING | Beginner |
| CASE | Intermediate |
| Subqueries | Intermediate |
| CTEs | Intermediate |
| UNION | Intermediate |
| EXISTS | Intermediate |
| Window Functions | Advanced |
| ROW_NUMBER() | Advanced |
| RANK() | Advanced |
| DENSE_RANK() | Advanced |
| LEAD() | Advanced |
| LAG() | Advanced |

---

# Example Query

Business Question

Which country generated the highest total sales?

```sql
SELECT
    Country,
    SUM(Sales) AS TotalSales
FROM sales_data
GROUP BY Country
ORDER BY TotalSales DESC;
```

Example Output

| Country | TotalSales |
|---------|-----------:|
| United States | 24,567,890 |
| Canada | 18,334,000 |
| France | 16,765,300 |

---

# Repository Structure

beginner/

Basic SQL syntax

intermediate/

More advanced filtering and query logic

advanced/

Analytical SQL using window functions and ranking

---

# Skills Demonstrated

✔ Data filtering

✔ Aggregations

✔ Business reporting

✔ Analytical SQL

✔ Window Functions

✔ Query optimization

✔ MySQL

---

# Why This Repository?

Many SQL tutorials explain syntax.

This repository focuses on solving real business problems using sales data similar to what analysts encounter in production environments.

Every query answers a practical question that could appear in dashboards, reports, or interviews.
