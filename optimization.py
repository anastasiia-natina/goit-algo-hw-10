import pulp as pl

x_lemonade = pl.Variable('lemonade', low=0, cat='Integer')
x_juice = pl.Variable('juice', low=0, cat='Integer')

objective = pl.maximize(x_lemonade + x_juice)

water_constraint = x_lemonade * 2 + x_juice * 1 <= 100
sugar_constraint = x_lemonade * 1 <= 50
lemon_juice_constraint = x_lemonade * 1 <= 30
fruit_puree_constraint = x_juice * 2 <= 40

model = pl.Problem('production_optimization')
model += objective
model += water_constraint
model += sugar_constraint
model += lemon_juice_constraint
model += fruit_puree_constraint

model.solve()

optimal_lemonade = pl.value(x_lemonade)
optimal_juice = pl.value(x_juice)

total_production = optimal_lemonade + optimal_juice

print(f"Оптимальна кількість 'Лимонаду': {optimal_lemonade}")
print(f"Оптимальна кількість 'Фруктового соку': {optimal_juice}")
print(f"Загальна кількість вироблених продуктів: {total_production}")

