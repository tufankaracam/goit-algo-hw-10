from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable


model = LpProblem(name="maximize-product", sense=LpMaximize)

L = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
F = LpVariable(name="Fruit_juice", lowBound=0, cat='Integer')

obj_func = L + F
model += obj_func

model += (2 * L + F <= 100, "Water_constraint")
model += (L <= 50, "Sugar_constraint")
model += (L <= 30, "Lemon_Juice_constraint")
model += (2 * F <= 40, "Fruit_Puree_constraint")

model.solve()
print("Solution Status:", LpStatus[model.status])
for variable in [L, F]:
    print(f"{variable.name} = {variable.varValue}")
print(f"Total number of products = {model.objective.value()}")
