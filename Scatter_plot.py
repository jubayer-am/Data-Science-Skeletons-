# =====================================================================
# SKELETON: PRODUCTION SCATTER PLOT ARCHITECTURE
# Use Case: Mapping relationship patterns, density, and outliers.
# =====================================================================
import matplotlib.pyplot as plt
import seaborn as sns
X_data=[2,4,6,7,8,13,16,15,20,12,6,16,17,18,12,14,13,16,19,17,12,15,16,17,13
,3,4,6,7,8,7,6,5,4,3,7,5,4,3,4,5,6,7,8,9,8,7,6,5,4,3,5,6,7,7,7,6,6,7,7,6,6,8][:60]
Y_data=[3,4,4,9,10,19,3,11,14,4,17,13,13,14,12.6,17,15,18,17,14.8,11,16,19,12,15,14,5,6,7,8,7,6,5,4,3,4,5,6,7,8,7,6,5,4,3,4,5,6,7,8,7,6,5,4,3,
6,7,8,6,4,5][:60]

# PHASE 1: Initialize System Foundations (The Canvas & Grid Box)
fig, ax = plt.subplots(figsize=(15,9))
# NEW ARCHITECTURE LAYER: THE SIMPLE GEOMETRIC BASELINE (Min to Max)
# =====================================================================
# Step A: Find the global minimum and maximum bounds across all data
absolute_min = min(min(X_data), min(Y_data))  # Lowest starting point
absolute_max = max(max(X_data), max(Y_data))  # Highest ending point


# Step B: Plot a single straight line connecting [min, max] to [min, max]
ax.plot(
   [absolute_min, absolute_max],  # X-coordinates for start & end
    [absolute_min, absolute_max],    # Y-coordinates for start & end
    color='red',
    linestyle='--',
    linewidth=3,
    label='Equal data Baseline (Y = X)'
)

# PHASE 2: Inject Structural Data Arrays
# - s: Controls marker area size (pixels)
# - alpha: Controls transparency (0 to 1) to reveal dense overlapping regions
# - edgecolors: Sets a distinct ring around markers to separate tight clusters
scatter_handle = ax.scatter(
    X_data,
    Y_data,
    color='violet',
    s=400,
    alpha=0.4,
    edgecolors='blue',
    label='data'
)

# PHASE 3: Structural Identification Layers
ax.set_title("Scatter Skeleton", fontsize=19, fontweight='bold', pad=18)
ax.set_xlabel("x data", fontsize=20, labelpad=10)
ax.set_ylabel("y data", fontsize=20, labelpad=10)
# =====================================================================


# PHASE 4: Layout Polishing & Interface Formatting
ax.grid(True, linestyle=':', alpha=1, color='green')
ax.legend(loc='upper left', frameon=True, fontsize=15, facecolor='lightblue', edgecolor='blue')

# PHASE 5: Clean Memory Allocation & Rendering
plt.tight_layout()
plt.show()
