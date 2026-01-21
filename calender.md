---
layout: default
title: Calendar and Age
---

This program prints today’s date and asks the user for their age.

```python
import datetime

today = datetime.date.today()
print("Today's date is:", today)

age = int(input("Enter your age: "))
print("Your age is", age, "years old.")
```
