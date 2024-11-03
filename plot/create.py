import os
import pandas as pd
import random

# Directory and file path relative to the script execution location
output_dir = os.path.join(os.path.dirname(__file__), '../hadoop_IO/input')
output_file = os.path.join(output_dir, 'input.txt')

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Generate random data for example (100 rectangles)
num_rectangles = 100
types = [1, 2, 3,4,5,6,7,8,9,10]
data = []
for _ in range(num_rectangles):
    rect_type = random.choice(types)
    left = random.randint(0, 100)
    bottom = random.randint(0, 100)
    width = random.randint(5, 20)
    height = random.randint(5, 20)
    right = left + width
    top = bottom + height
    data.append([rect_type, left, bottom, right, top])

# Create a DataFrame and save it to CSV
df = pd.DataFrame(data, columns=['type', 'left', 'bottom', 'right', 'top'])
df.to_csv(output_file, index=False)

print(f"File saved to {output_file}")
