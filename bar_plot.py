import matplotlib.pyplot as plt
import seaborn as sns

# 1. Prepare your data matrices
models = ['Logistic Regression', 'SVM', 'Random Forest', 'Neural Network']
accuracy_scores = [0.78, 0.84, 0.91, 0.95]

# 2. Set the structural design layout (clean, minimalist style)
plt.figure(figsize=(9, 5))
sns.set_theme(style="darkgrid")

# 3. Generate the bar plot
# Using a clean color palette ('viridis' or 'deep' looks highly professional)
ax = sns.barplot(x=models, y=accuracy_scores, palette="deep",hue=models,legend=False)

# 4. Format the axis labels and title structural strings
plt.title("Machine Learning Model Accuracy Comparison", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Model Architecture", fontsize=12, labelpad=10)
plt.ylabel("Accuracy Score (0.0 - 1.0)", fontsize=12, labelpad=10)

# 5. Set custom axis limits for data clarity
plt.ylim(0, 1)

# 6. Data Ingestion: Add exact value labels on top of each bar
for p in ax.patches:
    ax.annotate(f"{p.get_height():.5f}",
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 14),
                textcoords='offset points',
                fontsize=11, fontweight='bold')

# 7. Clean up layout margins and execute
plt.tight_layout()
plt.show()
