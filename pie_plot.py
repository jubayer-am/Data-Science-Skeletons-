import matplotlib.pyplot as plt

# 1. Prepare the data
labels = ['category A', 'Category B', 'Category C', 'Category D']
sizes = [35, 30, 20, 15]  # Percentages or absolute values
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Custom modern colors
explode = (0.05, 0, 0, 0)  # "Explode" or slightly separate the 1st slice

# 2. Create the pie chart
plt.figure(figsize=(6, 6))  # Ensures a square figure so the pie is a circle
plt.pie(
    sizes, 
    explode=explode, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%',  # Format to show one decimal percentage
    startangle=140,     # Rotate the start of the pie chart
    shadow=False        # True adds a 3D-like shadow
)

# 3. Customize and display
plt.title('My Simple Pie Chart', fontsize=14, fontweight='bold')
plt.tight_layout()  # Adjusts padding automatically
plt.show()
