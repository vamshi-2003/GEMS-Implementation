import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import os
# Load the rectangle data from input.txt
output_dir = os.path.join(os.path.dirname(__file__), '../hadoop_IO/input')
output_file = os.path.join(output_dir, 'input.txt')
data = pd.read_csv(output_file)

# Define a color map for different types
type_colors = {
    rect_type: plt.cm.tab10(i % 10)  # Tab10 colormap for distinct colors
    for i, rect_type in enumerate(data['type'].unique())
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each rectangle
for _, row in data.iterrows():
    rect_type = row['type']
    left = row['left']
    bottom = row['bottom']
    right = row['right']
    top = row['top']
    
    # Calculate width and height
    width = right - left
    height = top - bottom
    
    # Create a rectangle patch with color based on type
    rect = patches.Rectangle(
        (left, bottom), width, height, linewidth=1,
        edgecolor='black', facecolor=type_colors[rect_type]
    )
    
    # Add the rectangle to the plot
    ax.add_patch(rect)

# Add legend for rectangle types
handles = [
    patches.Patch(color=type_colors[rect_type], label=f'Type {rect_type}')
    for rect_type in type_colors
]
ax.legend(handles=handles)

# Set plot limits exactly to the min and max of rectangle coordinates
ax.set_xlim(data['left'].min(), data['right'].max())
ax.set_ylim(data['bottom'].min(), data['top'].max())

# Set labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Rectangles by Type")

# Show the plot
plt.show()
