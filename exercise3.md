---
layout: default
title: Exercise 3 – Time Conversion
---

This program converts time given in seconds into hours, minutes, and seconds.

```python
seconds = int(input("Enter time in seconds: "))

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(hours, "hours", minutes, "minutes", seconds, "seconds")
```
