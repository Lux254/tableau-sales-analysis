# tableau-sales-analysis
# **Tableau Sales Analysis Dashboard**

## **Background and Overview**
Sales data can often be messy and inconsistent, making it difficult to derive meaningful insights. This project focuses on cleaning a real-world sales dataset and visualizing key metrics using Tableau. The primary objective is to uncover trends in revenue, product demand, and customer payment preferences to inform better business decisions.

### **Key Objectives:**
- **Data Cleaning:** Handle missing values, correct errors, and standardize formats.
- **Sales Analysis:** Understand revenue distribution over time.
- **Product Performance:** Compare the quantity sold vs. revenue generated.
- **Customer Behavior:** Identify the most preferred payment methods.

---

## **Data Structure Overview**
The dataset originally contained missing values and inconsistencies, requiring extensive preprocessing before visualization. Below is an overview of the key fields in the dataset:

| Column Name            | Description                                       |
|------------------------|---------------------------------------------------|
| Transaction Date       | The date when the transaction occurred            |
| Item                   | The product sold                                  |
| Quantity               | Number of units sold                              |
| Total Spent            | Total revenue from the transaction                |
| Payment Method         | The method used by customers for payment          |
| Location               | In-store or Takeaway                              |

### **Data Cleaning Steps:**
- **Handled missing values**: Replaced `UNKNOWN`, `ERROR`, and null values appropriately.
- **Standardized date formats**: Ensured all transaction dates were correctly formatted.
- **Converted numerical columns**: Ensured values were in the correct data types.

---

## **Executive Summary**
After cleaning and analyzing the data, the following key findings emerged:

🔹 **Total Revenue Generated:** Approximately $7,000 per month, except for February, which had a total of about $11,000.  
🔹 **Top-Selling Product:** Juice emerged as the highest revenue-generating item, bringing in a total of $19,079. Despite not having the highest price per unit, its strong sales volume contributed significantly to overall revenue.
🔹 **Most Preferred Payment Method:** Digital Wallet (55%), followed by Cash (23%) and Credit Card (23%).  
🔹 **Month with Highest Sales:** February, due to an unusual spike on February 6th. 
🔹 **Sales by Location:** In-store sales generated $27,000, while takeaway sales accounted for $62,000, indicating a stronger preference for takeaway purchases.

---

## **Insights Deep Dive**
### **Revenue Distribution Over Time**
- The line graph visualization shows how revenue fluctuates across different months.
- Sales for all months were similar, averaging about 7,000.
- An anomaly was observed on February 6th, where sales peaked at $4,000 in a single day, compared to the usual daily average of $200.

### **Quantity vs. Amount Generated**
- Juice was the best-selling item in terms of total units sold (6,438) and also generated the highest revenue ($19,079). Despite having a lower price per unit ($3), its high demand contributed significantly to overall revenue.
- Salad, priced at $4.9 per unit, had fewer sales (3,471 units) but still generated $17,365 in revenue, showing that higher-priced items can contribute strongly to total earnings.
- Sandwich followed a similar pattern with a price of $4 per unit, 3,430 units sold, and a total revenue of $13,751.
- This analysis highlights the importance of balancing pricing strategy and demand to optimize revenue generation.
- Some high-selling products do not generate the highest revenue.
- The bar-in-bar chart compares the number of units sold against total revenue.

### **Payment Method Preferences**
- Digital Wallet was the most preferred payment method, accounting for 55% of transactions.
- Cash and Credit Card usage were both at 23%.

---

## **Recommendations**
Based on the insights derived from the data, the following recommendations can be made:

✅ **Investigate the February 6th anomaly** to understand what caused the spike in sales and whether similar strategies can be replicated.  
✅ **Increase stock for high-demand products**, particularly Juice, which generated the highest revenue due to strong sales volume.
✅ **Optimize pricing strategies** for high-value but lower-selling products like Salad and Sandwich, which have higher per-unit prices but lower total sales.
✅ **Encourage alternative payment methods** by offering incentives for Digital Wallet users, as it is already the most preferred method (55%). 
✅ **Expand takeaway services** by improving packaging, offering more convenient pickup options, or enhancing delivery partnerships to capitalize on the growing demand for takeaway sales.  
