import numpy as np
import random
import scipy.intagrate as spi
import matplotlib.pyplot as plt

def f(x):
    return x ** 2
a = 0 
b = 2
N = 10000

sum_y = 0
area = 0

for i in range(N):
    x = random.uniform(a, b)

    y = f(x)
    dx = (b - a) / N
    area += y * dx
    sum_y += y

average_y = sum_y / N

integral_estimate = average_y * (b - a)

print(f"Оцінка інтеграла за методом Монте-Карло: {integral_estimate}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

result, error = spi.quad(f, a, b)

print(f"Інтеграл за допомогою quad: {result}")

