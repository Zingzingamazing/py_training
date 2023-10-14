## Weight converter
## error missing
## 第一步输入要限制为数字，不是数字需要循环
## 第二步输入错时要循环
weight = input("Weight: ")
code = input("L OR K")

if code == "l":
    weight = float(weight) * 0.5
    print(weight)
elif code == "k":
    weight = float(weight) *2
    print(weight)
else:
    print("again")

    

