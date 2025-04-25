import pandas as pd
from datetime import datetime, time

# a) Date time object for Jan 15 2012
dt_a = pd.to_datetime("2012-01-15")
print("a) Date time object for Jan 15 2012:", dt_a)

# b) Specific date and time of 9:20 pm
dt_b = pd.to_datetime("2023-01-01 21:20")  # Example date with time
print("b) Specific date and time of 9:20 PM:", dt_b)

# c) Local date and time (now)
dt_c = pd.Timestamp.now()
print("c) Local date and time:", dt_c)

# d) A date without time
dt_d = pd.to_datetime("2023-04-14").date()
print("d) Date without time:", dt_d)

# e) Current date
dt_e = pd.Timestamp.now().date()
print("e) Current date:", dt_e)

# f) Time from a datetime
dt_f = pd.Timestamp.now().time()
print("f) Time from a datetime:", dt_f)

# g) Current local time
dt_g = datetime.now().time()
print("g) Current local time:", dt_g)
