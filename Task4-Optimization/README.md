# 📊 Product Mix Optimization using Linear Programming

## 📌 Overview

This project solves a real-world business problem using **Linear Programming**.
A furniture factory produces chairs and tables and aims to maximize profit under limited resources.

---

## 🧠 Problem Statement

The factory produces:

* Chairs → Profit: $50 per unit
* Tables → Profit: $120 per unit

### Resource Requirements:

| Product | Wood (kg) | Labor (hrs) |
| ------- | --------- | ----------- |
| Chair   | 2         | 3           |
| Table   | 5         | 4           |

### Available Resources:

* Wood: 200 kg
* Labor: 180 hours

---

## 🎯 Objective

Maximize total profit while satisfying resource constraints.

---

## ⚙️ Approach

* Modeled the problem using Linear Programming
* Implemented using the PuLP library in Python
* Defined decision variables, objective function, and constraints
* Solved using an optimization solver

---

## 📊 Visualizations

* Production quantities of chairs and tables
* Resource utilization (used vs available)

---

## 💡 Business Insights

* Identifies the optimal production mix
* Highlights resource utilization
* Helps in understanding constraints and bottlenecks

---

## 🚀 Technologies Used

* Python
* PuLP
* Matplotlib
* NumPy

---

## ▶️ How to Run

1. Install dependencies:

   ```
   pip install pulp matplotlib numpy
   ```

2. Run the script:

   ```
   python task4_optimization.py
   ```

3. Output:

   * Console results
   * Saved visualization (`optimization_results.png`)

---

## 👩‍💻 Author

Priyanshi Bagde
Data Science Intern
