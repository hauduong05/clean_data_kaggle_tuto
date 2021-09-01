import numpy as np
from mlxtend.preprocessing import minmax_scaling
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

original_data = np.random.exponential(size=1000)
scaled_data = minmax_scaling(original_data, columns=[0]) # scale data
normalized_data = stats.boxcox(original_data) # normalize data

fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.set_title('original_data')
sns.displot(original_data, ax=ax1)
ax2.set_title('scaled_data')
sns.displot(scaled_data, ax=ax2)
ax3.set_title('normalized_data')
sns.displot(normalized_data, ax=ax3)
plt.show()