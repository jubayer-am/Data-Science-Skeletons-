import matplotlib.pyplot as plt
import numpy as np

# dummy data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,9,8,7,6,5,10,4,3,5,1,7]

# 2. Create the histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=4, color='skyblue', edgecolor='green')

# 3. Add labels and title
plt.title('Distribution of Exam Scores', fontsize=14)
plt.xlabel('Scores (Continuous Intervals)', fontsize=12)
plt.ylabel('Count of Students (Frequency)', fontsize=12)

# 4. Display the plot
plt.tight_layout()
plt.show()















