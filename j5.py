import numpy as np
from tabulate import tabulate
from astropy.table import Table

x = np.linspace(0, 2, 1000)
y = np.sin(x)

table_data = [(a, b) for a, b in zip(x, y)]

table_headers = ["x", "sin(x)"]
python_table = tabulate(table_data, tablefmt="grid", headers=table_headers, floatfmt=".3f")

astropy_table = Table()
astropy_table["x"] = x
astropy_table["sin(x)"] = y

astropy_table["x"].format = "{:.3f}"
astropy_table["sin(x)"].format = "{:.3f}"

def main():
    print(astropy_table)

if __name__=='__main__':
    main()
  
