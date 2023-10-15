## Weight converter
## error missing
## 第一步输入要限制为数字，不是数字需要循环
## 第二步输入错时要循环
weight = input("Weight: ")
code = input("L OR K")

if code.upper == "L":
    weight = float(weight) * 0.45
    print(weight)
elif code.upper == "K":
    weight = float(weight) / 0.45
    print(weight)
else:
    print("again")

    

