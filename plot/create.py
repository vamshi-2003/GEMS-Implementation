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
types = ['P','Q','R','S']
data = []
width_l=150
height_l=75
for _ in range(num_rectangles):
    rect_type = random.choice(types)
    left = random.randint(0, 1000-width_l)
    bottom = random.randint(0, 1000-width_l)
    width = random.randint(50, width_l)
    height = random.randint(50, height_l)
    #at random swap width and height
    extra=random.randint(0,width_l-height_l)
    bottom+=extra
    if random.random() >= 0.5:
        width, height = height, width
        left+=extra
        bottom-=extra

    right = left + width
    top = bottom + height
    data.append([rect_type, left, bottom, right, top])

# Create a DataFrame and save it to CSV
df = pd.DataFrame(data, columns=['type', 'left', 'bottom', 'right', 'top'])
df = df.sort_values(by='type')
df.to_csv(output_file, index=False)

print(f"File saved to {output_file}")
