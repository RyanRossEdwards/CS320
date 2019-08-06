import sys
# import pandas as pd
import numpy as np

# Can test with $ python a1.py < input

# Capture stdin
full_input = []

for line in sys.stdin:
    try:
        array = ([int(x) for x in line.split()])
        full_input += [array]
        if array == [0,0]:
            break
    except:
        continue

print(full_input, '\n')

# Turn the inputs into 2D arrays
grids = []
new_grid = True

for i in range(len(full_input)-1):
    if new_grid:
        new_grid = False
        dimensions = full_input[i]
        dimension_total = i + dimensions[0]
        print(dimensions)
    
    elif not new_grid and i < dimension_total:
        print(i)
        continue

    else:
        new_grid = True
        print(i)
        continue