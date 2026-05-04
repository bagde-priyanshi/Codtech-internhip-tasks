from dataclasses import dataclass
from typing import Dict, Tuple
import pulp


@dataclass
class Product:
    name: str
    profit: int
    wood: int
    labor: int


def build_optimizer() -> Tuple[pulp.LpProblem, Dict[str, pulp.LpVariable], Dict[str, Product], Dict[str, int]]:
    resources = {"wood": 200, "labor": 180}
    products = {
        "chair": Product("Chair", profit=50, wood=2, labor=3),
        "table": Product("Table", profit=120, wood=5, labor=4),
    }

    plan = pulp.LpProblem("Furniture_Profit_Planner", pulp.LpMaximize)

    units = {
        key: pulp.LpVariable(f"units_{key}", lowBound=0, cat="Integer")
        for key in products
    }

    plan += pulp.lpSum(products[key].profit * units[key] for key in products), "net_profit"
    plan += pulp.lpSum(products[key].wood * units[key] for key in products) <= resources["wood"], "wood_limit"
    plan += pulp.lpSum(products[key].labor * units[key] for key in products) <= resources["labor"], "labor_limit"

    return plan, units, products, resources


def solve_and_report() -> None:
    plan, units, products, resources = build_optimizer()
    status = plan.solve(pulp.PULP_CBC_CMD(msg=False))
    status_text = pulp.LpStatus[status]

    print("=" * 64)
    print("TASK 4 - PRODUCT OPTIMIZATION FOR FURNITURE FACTORY")
    print("=" * 64)
    print(f"Solver status             : {status_text}")

    if status_text != "Optimal":
        print("Warning: an optimal solution was not found. Please review the model or constraints.")
        return

    values = {key: int(pulp.value(var)) for key, var in units.items()}
    total_profit = int(pulp.value(plan.objective))
    wood_used = sum(products[key].wood * values[key] for key in products)
    labor_used = sum(products[key].labor * values[key] for key in products)

    print(f"Optimal chairs to produce : {values['chair']}")
    print(f"Optimal tables to produce : {values['table']}")
    print(f"Maximum profit            : ${total_profit}")

    print("\nResource utilization")
    print(f"Wood used                 : {wood_used} / {resources['wood']} kg")
    print(f"Labor used                : {labor_used} / {resources['labor']} hrs")
    print(f"Unused wood               : {resources['wood'] - wood_used} kg")
    print(f"Unused labor              : {resources['labor'] - labor_used} hrs")

    print("\nBusiness interpretation")
    if resources['wood'] - wood_used == 0:
        print("- Wood is fully utilized, so it is a binding resource.")
    if resources['labor'] - labor_used == 0:
        print("- Labor is fully utilized, so it is a binding resource.")
    print("- This plan gives the highest profit without crossing resource limits.")

if __name__ == "__main__":
    solve_and_report()
