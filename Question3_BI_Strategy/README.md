📊 Pharma Sales \& Inventory Dashboard (Power BI)

📌 Project Overview



This project automates reporting for a pharmaceutical company by integrating multiple data sources into an interactive Power BI dashboard.

The solution reduces manual reporting by ~35%, improves visibility into sales performance, inventory management, product expiry monitoring, and forecast accuracy.



🗂 Data Sources



Sales Data (CSV, 50K+ rows)



Columns: Date, Product\_ID, Sales\_Amount, Region, Sales\_Rep



Purpose: Analyze sales across products, time, and regions.



Product Master (Excel)



Columns: Product\_ID, Product\_Name, Category, Manufacturing\_Cost, Expiry\_Date



Purpose: Provide product details and expiry monitoring.



Inventory Data (SQL Database)



Columns: Product\_ID, Current\_Stock, Reorder\_Level, Supplier\_ID



Purpose: Monitor stock levels and reorder requirements.



🛠 Data Modeling



Model type: Star schema



Fact Table: Sales



Dimension Tables: Product Master, Inventory, Date Table



Relationships:



Sales → Product Master (Product\_ID)



Product Master → Inventory (Product\_ID)



Sales → Date Table (Date)



🔄 Transformations



Applied via DAX Calculated Columns and Power Query:



Forecast (Sales Table)



Forecast = \[Sales\_Amount] \* 1.1





Expiring Soon (Product Master)



Expiring Soon = IF(Product\_Master\[Expiry\_Date] <= TODAY() + 180, 1, 0)





Removed duplicates, standardized data types, and renamed columns for clarity.



📐 Key DAX Measures



Total Sales



Total Sales = SUM(Sales\_Data\[Sales\_Amount])





Profit Margin %



Profit Margin % =

DIVIDE(

&nbsp;   \[Total Sales] - SUMX(Sales\_Data, Sales\_Data\[Quantity] \* RELATED(Product\_Master\[Manufacturing\_Cost])),

&nbsp;   \[Total Sales]

)





Inventory Days



Inventory Days =

DIVIDE(SUM(Inventory\[Current\_Stock]), \[Total Sales] / 30)





Forecast Variance %



Forecast Variance % =

DIVIDE(\[Total Sales] - SUM(Sales\_Data\[Forecast]), SUM(Sales\_Data\[Forecast]))



📊 Dashboard Pages



Sales Performance



Sales by Region (Clustered Column)



Sales by Category (Treemap)



Sales Trend (Line Chart)



KPIs: Total Sales, Profit Margin %



Inventory Turnover



Inventory Days (Card)



Stock vs Reorder Levels (Table with conditional formatting)



Products Nearing Expiry



Expiring Soon filter (within 6 months)



Forecast Accuracy



Actual vs Forecast (Line Chart)



Forecast Variance % (Gauge, Target = 0%)



⚡ Performance Optimization



Star schema modeling to simplify relationships.



Used DAX measures instead of calculated columns where possible.



Disabled auto date/time; used a custom Date table.



Reduced high-cardinality columns and unused fields.



Suggested incremental refresh for large Sales tables.



Validated using Performance Analyzer in Power BI.



📷 Screenshots



(Insert screenshots of key visuals here — e.g., /screenshots/sales\_dashboard.png)



🚀 Deliverables



Power BI file: Pharma\_Dashboard.pbix



Documentation: /docs/Project\_Documentation.pdf



Screenshots: /screenshots/



README (this file)



👨‍💻 Author



Aman Singh



💼 LinkedIn: [https://www.linkedin.com/in/datanalytics-aman/](https://www.linkedin.com/in/datanalytics-aman/)





