# Optimization of Collection and Distribution Networks in Recycling Logistics

This project focuses on the strategic design and optimization of a reverse logistics network for recyclable waste. It integrates Multi-Criteria Decision Making (MCDM) methods with Mathematical Programming to minimize costs and maximize efficiency in waste collection and distribution.

## Project Overview
The goal is to design a robust reverse logistics network that handles electronic waste, plastics, and metal components. The study employs a hybrid approach:
1.  **AHP (Analytic Hierarchy Process):** To determine the importance weights of selection criteria.
2.  **TOPSIS:** To rank and select the most suitable facility locations.
3.  **Mathematical Optimization:** To minimize the total cost of transportation, facility operation, and processing.

## Methodology & Mathematical Model

### 1. Multi-Criteria Decision Making (AHP & TOPSIS)
We evaluated potential facility locations based on several criteria including:
* Proximity to waste generation points
* Transportation infrastructure
* Operational costs
* Environmental impact

### 2. Objective Function
The core of the model is a Mixed-Integer Linear Programming (MILP) formulation aimed at minimizing total network cost ($Z$):

$$\min Z = \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij} + \sum_{j \in J} f_j y_j$$

*Where:*
* $c_{ij}$: Unit transportation cost from collection point $i$ to facility $j$.
* $x_{ij}$: Quantity of waste transported.
* $f_j$: Fixed cost of opening facility $j$.
* $y_j$: Binary variable (1 if facility $j$ is opened, 0 otherwise).

### 3. Key Constraints
* **Demand Satisfaction:** All generated waste must be collected.
* **Capacity Limits:** Total waste processed at facility $j$ cannot exceed its capacity $Cap_j$.
* **Flow Conservation:** Ensuring the balance between incoming collection and outgoing distribution.

## Results & Analysis
Based on the analysis across multiple scenarios (Scenario 1-4):
* **Optimal Location Selection:** The model identified the most cost-effective hubs for recycling operations.
* **Cost Savings:** Strategic facility placement resulted in a significant reduction in total logistics mileage.
* **Sensitivity Analysis:** Evaluated how changes in waste volume impact the stability of the network.

## Project Structure
* `/Docs`: Detailed mathematical proofs and process explanations.
* `/Data`: Input parameters for AHP, TOPSIS, and optimization scenarios.
* `README.md`: Project summary and documentation (You are here).

## Tools Used
* **Decision Support:** AHP & TOPSIS Methods.
* **Analysis:** Microsoft Excel (Advanced modeling & Data Tables).
* **Modeling:** Optimization Theory & Logistics Network Design.
