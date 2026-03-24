# Aviation Operations Performance Engine (A350 Focus)

## ✈️ Project Overview
This repository contains a Python-based analytical engine designed to optimize **Airbus A350 Turnaround Efficiency** and monitor **Fuel Variances**. Built specifically for airline operations management, the tool transforms raw flight logs into actionable insights to improve On-Time Performance (OTP) and reduce operational "leakage."

## 📊 Business Objectives
* **Minimize Turnaround Leakage:** Identify and quantify the financial impact of ground delays.
* **Root Cause Identification:** Categorize operational bottlenecks (Ground Handling, Catering, Refueling).
* **Fuel Variance Monitoring:** Analyze discrepancies between planned and actual fuel uplift to drive sustainability and cost savings.
* **KPI Visualization:** Provide a high-level Looker Studio dashboard for senior stakeholders.

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
