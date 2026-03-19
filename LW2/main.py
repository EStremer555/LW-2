import math


eps = 0.001
max_iter = 100

print("Метод простої ітерації:")

x1 = x2 = x3 = 0

for i in range(max_iter):
    x1_new = (5.0 - 3.1*x2 - 4.0*x3) / 3.7
    x2_new = (4.9 - 4.1*x1 + 4.8*x3) / 4.5
    x3_new = (2.7 + 2.1*x1 + 3.7*x2) / 1.8

    if max(abs(x1_new-x1), abs(x2_new-x2), abs(x3_new-x3)) < eps:
        break

    x1, x2, x3 = x1_new, x2_new, x3_new

print("x1 =", round(x1_new,3), "\nx2 =", round(x2_new,3), "\nx3 =", round(x3_new,3), "\nКількість ітерацій:", i+1)



print("\nМетод Зейделя:")

x1 = x2 = x3 = 0

for i in range(max_iter):

    x1_new = (5.0 - 3.1*x2 - 4.0*x3) / 3.7
    x2_new = (4.9 - 4.1*x1_new + 4.8*x3) / 4.5
    x3_new = (2.7 + 2.1*x1_new + 3.7*x2_new) / 1.8

    # перевірка на nan або дуже великі числа
    if math.isnan(x1_new) or math.isnan(x2_new) or math.isnan(x3_new):
        print("Метод розійшовся (отримано NaN)")
        break

    if max(abs(x1_new-x1), abs(x2_new-x2), abs(x3_new-x3)) < eps:
        break

    x1, x2, x3 = x1_new, x2_new, x3_new

else:
    print("Метод не збігся за", max_iter, "ітерацій")
    x1_new, x2_new, x3_new = x1, x2, x3

print("x1 =", round(x1_new,3), "\nx2 =", round(x2_new,3), "\nx3 =", round(x3_new,3), "\nКількість ітерацій:", i+1)
