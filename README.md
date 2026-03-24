# Aviation Operations Performance Engine (A350 Focus)

## ✈️ Project Overview
This repository contains a Python-based analytical engine designed to optimize **Airbus Sustainability50 (A350-1000) Turnaround Efficiency** and monitor **Fuel Variances**. Built specifically for airline operations management, the tool transforms raw flight logs into actionable insights to improve On-Time Performance (OTP) and reduce operational "leakage."

## 📊 Project Objectives
* **Minimize Turnaround Leakage:** Identify and quantify the financial impact of ground delays.
* **Root Cause Identification:** Categorize operational bottlenecks (Ground Handling, Catering, Refueling).
* **Fuel Variance Monitoring:** Analyze discrepancies between planned and actual fuel uplift to drive sustainability and cost savings.
* **KPI Visualization:** Provide a high-level Looker Studio dashboard for senior stakeholders.

## 💰 Business Impact
Implementing this performance engine provides tangible value to airline operations across three primary pillars:

* **Cost Containment:** By identifying "Turnaround Leakage," the business can pinpoint specific ground handling inefficiencies that lead to overtime costs and airport penalties. Every 1% improvement in turnaround efficiency can save millions in annual operating expenditure (OPEX).
* **Asset Utilization:** Maximizing the "Time in Air" for the Airbus A350 fleet. Reducing ground time increases the available block hours per aircraft, allowing for higher frequency on high-demand routes without increasing fleet size.
* **Data-Driven Vendor Management:** Moves contract discussions from anecdotal evidence to hard data. Monthly Performance Reviews (MPRs) with ground handlers are backed by "Root Cause" evidence, ensuring accountability and driving sustainable change.

## 📈 Key Performance Indicators (KPIs)
The success of the **Aviation Operations Performance Engine** is measured by the following metrics, tracked in **UAE Dirhams (AED)** for financial precision:

| KPI | Strategic Objective | Metric Definition |
| :--- | :--- | :--- |
| **On-Time Performance (OTP)** | Operational Excellence | % of flights departing within 15 minutes of Scheduled Departure Time (STD). |
| **TAT Leakage (Financial)** | Cost Reduction | The total calculated cost of delay minutes (R) categorized by controllable vs. uncontrollable factors. |
| **Fuel Uplift Variance** | Sustainability | The % difference between the Flight Plan (OFP) required fuel and the actual uplifted fuel. |
| **Vendor Turnaround Index** | Efficiency | A weighted score ranking ground handlers based on their ability to meet the "Clean Turnaround" window. |
| **RCA Accuracy** | Process Improvement | The % of delayed flights successfully mapped to a specific Root Cause (Catering, Fuel, Tech, etc.). |

## ⚙️ Installation & Usage
1. Clone the repository: `git clone https://github.com/m-yusri-ajam/aviation-ops-performance-engine`
2. Create a virtual environment: `python3 -m venv venv`
3. Install dependencies: `pip install pandas` (Note: Looker Studio handles the visualization)
4. Generate the logs: `python3 src/data_generator.py`
5. Process the KPIs: `python3 src/analyzer.py`

📊 [Live Operational Dashboard](https://lookerstudio.google.com/reporting/50a15298-e043-41fc-92b0-2baacec1706a)

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Environment:** Linux (Ubuntu)
* **Visualization:** Looker Studio (via Master CSV Export)
* **Methodology:** Root Cause Analysis (RCA) & Agile Project Management

## 📂 Repository Structure
```text
aviation-ops-performance-engine/
├── data/               # Synthetic flight logs and ground data
├── docs/               # Project Charter and KPI Definitions
├── src/                # Python logic for Turnaround & Fuel Analysis
├── reports/            # Exported CSVs for Looker Studio
└── README.md           # Project Documentation
