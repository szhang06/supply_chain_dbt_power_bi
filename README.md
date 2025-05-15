# 🏭 Supply Chain Optimization using DBT & Power BI

## 🚀 Purpose of the Project

This project addresses a real-world business problem: **inefficient supply chain operations** in a manufacturing company. By combining modern data engineering (with DBT) and dynamic business intelligence (via Power BI), the goal is to:

- Identify inefficiencies in inventory and logistics as well as customer behaviors.
- Deliver actionable insights for cost reduction and improved operations.
- Showcase how data transformation and visualization can drive smarter decisions.

---

## 🔧 Tech Stack

- **BigQuery**: – Cloud-based data warehouse     
- **DBT (Data Build Tool)** – Data transformation, testing, and documentation.
- **Power BI** – Interactive dashboards for business insight.
- **SQL** – Core logic for data modeling.
- **Git & GitHub** – Version control and collaboration.
- **GitHub Actions** – CI/CD pipelines for DBT models.

---

## 🧠 Business Problem: Supply Chain Inefficiency

A global manufacturer faced rising costs and inconsistent supply chain performance. Key challenges included:

- **Supplier delays and variability** disrupting production
- **High logistics costs** without clear visibility into causes

---

## 🧩 The Solution

### DBT Pipeline

Using DBT, raw supply chain data was transformed into clean, analytics-ready datasets:

- **Staging Models** – Standardized raw data into consistent formats
- **Intermediate Models** – Normalized data into dimensional and facual tables.
- **Mart Models** – Provided high-level summaries for Power BI consumption

#### ✅ DBT Highlights

| Skill | Description |
|-------|-------------|
| **Data Modeling** | Built layered architecture (staging → intermediate → marts) |
| **Data Testing** | Implemented freshness, uniqueness, and null checks |
| **CI/CD** | Configured **GitHub Actions** to run `dbt run` and `dbt test` on every pull request |
| **Documentation** | Auto-generated model documentation and lineage graphs |
| **Jinja & Macros** | Wrote reusable logic for dynamic modeling and filters |

---

### Power BI Dashboard [ to be updated]

The Power BI report visualizes key supply chain metrics, enabling decision-makers to quickly identify bottlenecks and improvement areas.

#### 📊 Dashboard Highlights

- **Inventory Heatmaps** – Identify overstock/understock trends by region and product
- **Supplier Scorecards** – Track on-time delivery, lead time variance, and defect rates
- **Logistics Spend Analysis** – Drill down into transportation costs by route, carrier, and warehouse

![dashboard](./images/dashboard_screenshot.png) <!-- Replace with actual image if available -->

---

## 📈 Key Business Insights

- **15% of SKUs are chronically overstocked**, tying up $2M in excess inventory
- **3 suppliers have >25% late deliveries**, creating production delays
- **Southeast region incurs 20% higher logistics costs** due to inefficient routing

---

## 💡 Recommendations

1. **Adopt Just-in-Time inventory policies** to reduce holding costs
2. **Diversify supplier base** to reduce dependency and improve lead time
3. **Optimize routing plans** to balance cost and delivery speed across regions

---

## 🛠️ How to Run the Project

### Prerequisites

- DBT CLI installed ([Install Guide](https://docs.getdbt.com/dbt-cli/installation))
- Power BI Desktop installed
- A SQL database connection (PostgreSQL, Snowflake, etc.)

### Instructions

```bash
# Clone the repo
git clone https://github.com/szhang06/supply_chain_dbt_power_bi.git
cd supply_chain_dbt_power_bi

# Install DBT dependencies
dbt deps

# Configure your DBT profile (~/.dbt/profiles.yml)

# Run the transformation pipeline
dbt run
dbt test

