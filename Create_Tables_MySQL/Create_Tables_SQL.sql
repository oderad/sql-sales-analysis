CREATE TABLE seg_dim (
    Seg_Key VARCHAR(10) PRIMARY KEY,
    Segment VARCHAR(50)
) ENGINE=InnoDB;

CREATE TABLE country_dim (
    Coun_Key VARCHAR(50) PRIMARY KEY,
    Country VARCHAR(50)
) ENGINE=InnoDB;

CREATE TABLE prod_dim (
    Prod_Key VARCHAR(10) PRIMARY KEY,
    Product VARCHAR(20),
    Manufacturing_Price DECIMAL(10,2)
) ENGINE=InnoDB;


CREATE TABLE sales_fct (
    Sales_ID VARCHAR(10) PRIMARY KEY,
    Seg_Key VARCHAR(10),
    Cty_Key VARCHAR(50),
    Prd_Key VARCHAR(10),
    Discount_Band VARCHAR(20),
    Units_Sold INT,
    Sale_Price DECIMAL(10,2),
    Gross_Sales DECIMAL(12,2),
    Discounts DECIMAL(12,2),
    Sales DECIMAL(12,2),
    COGS DECIMAL(12,2),
    Profit DECIMAL(12,2),
    Date DATE,

    FOREIGN KEY (Seg_Key) REFERENCES seg_dim(Seg_Key),
    FOREIGN KEY (Cty_Key) REFERENCES country_dim(Coun_Key),
    FOREIGN KEY (Prd_Key) REFERENCES prod_dim(Prod_Key)
) ENGINE=InnoDB;
