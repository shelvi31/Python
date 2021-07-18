import pandas as pd
import functools

data = [{"d1": "s1", 
		"ts":"2020-01-01 19:00:00"},
		{"d2": "s1", 
		"ts":"2020-01-01 19:10:51"},
		{"d3": "s1", 
		"ts":"2021-02-31 19:20:50"},
		{"d4": "s1", 
		"ts":"2019-01-01 19:18:59"}]
	
list = []
for i in range(len(data)):
    for key,value in data[i].items():
        if key == "ts":
            list.append(value)

sorted = sorted(list)
print(sorted)