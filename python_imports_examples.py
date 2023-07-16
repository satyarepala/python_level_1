# organized_imports.py

# Group imports based on their source
import os
import sys

import requests
import pandas as pd

# Use explicit imports instead of wildcard imports
# Avoid: from math import *
from math import sqrt, sin, cos
# Avoid: from random import *
from random import randint

# Group related functions or classes together
# Math-related functions
from math import floor, ceil
# Data processing functions
import pandas as pd
# Plotting functions
import matplotlib.pyplot as plt

# Use aliases for long or commonly used module names
# Avoid: import pandas
# Prefer: import pandas as pd
import pandas as pd
# Avoid: import matplotlib.pyplot
# Prefer: import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Avoid importing unnecessary modules
# Only import the needed functions from os
from os import path, mkdir

# Imports within functions (conditional imports)
def some_function():
    if some_condition:
        # Import only when needed
        import module_to_import
        # Use the imported module
        module_to_import.some_function()

# Main code starts here...
# You can use the imported functions and modules in your code
