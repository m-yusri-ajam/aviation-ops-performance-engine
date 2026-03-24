# Project Charter: A350 Operations Performance Engine

## 1. Project Purpose & Background
<div style="text-align: justify;">
Etihad's <b>2030 Vision</b> involves a significant fleet growth, centered around the Airbus A350, or more affectionately known as the <b>Sustainability50</b>. As flight frequency continues to increase, minor inefficiencies in ground handling and fuel management could compound into massive financial <i>leakage</i>. This project initiates the development of an automated analytical engine to apply Root Cause Analysis in finding the cause of turnaround delays and fuel variances, which shifts operations from reactive to proactive management. </div>

## 2. Project Objectives
<div style="text-align: justify;">
<ul><li><b>Automate Data Ingestion:</b> Connect and normalize disparate flight logs and ground handling within the first 30 days.</li>
<li><b>Reduce Manual Reporting:</b> Replace manual Excel-based turnaround tracking with a real-time dashboard created in <b>Looker Studio</b>.</li>
<li><b>Identify Cost Savings:</b> Pinpoint the top 3 ground handling bottlenecks to target a <b>5% reduction in TAT (Turnaround Time) Leakage</b> within the first quarter of deployment.</li></ul>
</div>

## 3. Stakeholder Map
| **Stakeholder** | **Role** | **Interest/Expectation** |
|---|---|---|
| **VP Operations** | Project Sponsor | High-level OTP (On-Time Performance) and cost reduction. |
| **Fuel Procurement Manager** | Key Stakeholder | Accuracy in fuel uplift vs. plan to manage hedging and sustainability goals. |
| **Ground Handling Vendors** | External Partner | Data-backed performance reviews and clear KPI targets. |
| **Digital/IT Team** | Support | Data security, API security, and Linux environment compatibility. |

## 4. Project Scope
<div style="text-align: justify;"><ul>
<li><b>In-Scope:</b> A350-1000 fleet data, fuel uplift analysis, turnaround root cause categorization, financial impact calculation in <b>Dirhams (AED)</b>.</li>
<li><b>Out-of-Scope:</b> In-flight entertainment (IFE) data, passenger manifest details, or long-term maintenance scheduling (MRO).</ul></div>

## 5. Risk Register
| **Risk** | **Impact** | **Mitigation Strategy** |
|---|---|---|
| **Data Silos** | High | Use Python (pandas) to create a unified schema for different vendor formats. |
| **Sensor/API Downtime** | Medium | Implement local caching and "Last Known State" logic in the Python engine. |
| **User Adoption** | Medium | Involve ground handling leads early in the dashboard design phase (Agile feedback). |

## 6. Project Timeline (Milestones)
<div style="text-align: justify;"><ul><li><b>Phase 1 (Initiation):</b> Charter approval and Repo setup.</li>
<li><b>Phase 2 (Development):</b> Python engine build and synthetic data stress-testing.</li>
<li><b>Phase 3 (Visualization):</b> Looker Studio dashboard integration.</li>
<li><b>Phase 4 (Review):</b> Final ROI analysis and project handover.</li></ul></div>