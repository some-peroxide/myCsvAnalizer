import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv('D:/publisher27AUG-1.csv')

ax1 = df.plot(kind = 'line', x = 'Time', y = 'Average Sent Messages', color = 'blue')
ax2 = df.plot(kind = 'line', x = 'Time', y = 'Average Elapsed', secondary_y=True, color = 'green', ax=ax1)
ax1.set_ylabel('Average Sent Messages')
ax2.set_ylabel('Average Elapsed(ms)')
plt.show()