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
    rect_type: plt.cm.hsv(i / len(data['type'].unique()))
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

#-----------------------------------------------------------------
# Set plot limits exactly to the min and max of rectangle coordinates
x_min, x_max = 0, 1000
y_min, y_max = 0, 1000
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Calculate the center point for dividing lines
x_center = (x_min + x_max) / 2
y_center = (y_min + y_max) / 2

# Draw the dividing lines
ax.axvline(x=x_center, color='black', linestyle='-', linewidth=1)
ax.axhline(y=y_center, color='black', linestyle='-', linewidth=1)

# Label each Cell
bbox_props = dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white')
ax.text(x_center-250, y_center-15, 'Cell 1', ha='center', va='top', fontsize=20, color='black', bbox=bbox_props)
ax.text(x_max-250, y_center -15, 'Cell 2', ha='center', va='top', fontsize=20, color='black', bbox=bbox_props)
ax.text(x_center-250, y_max-15 , 'Cell 3', ha='center', va='top', fontsize=20, color='black', bbox=bbox_props)
ax.text(x_max -250, y_max -15, 'Cell 4', ha='center', va='top', fontsize=20, color='black', bbox=bbox_props)
#-----------------------------------------------------------------
# Set labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Rectangles by Type")

# used to improve layout, especially if labels or legends are crowded.
fig.tight_layout()
# Show the plot
plt.show()
