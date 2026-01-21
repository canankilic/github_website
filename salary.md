---
layout: default
title: Salary Calculator
---

This program calculates salary components and prints gross and net salary.

```python
basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12

gross_salary = basic + hra + da
net_salary = gross_salary - pf

print("HRA =", hra)
print("DA =", da)
print("PF =", pf)
print("Gross salary =", gross_salary)
print("Net salary =", net_salary)
```
