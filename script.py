import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
#print(digits.data)
#print(digits.target)

#print(digits.target[100])
#plt.gray() 
#plt.matshow(digits.images[100])
#plt.show()

model = KMeans(n_clusters = 10, random_state=42)

model.fit(digits.data)


new_samples = np.array([
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.22,1.45,0.07,0.00,0.00,0.00,0.00,0.00,6.17,6.76,4.46,0.00,0.00,0.00,0.00,0.00,0.00,0.69,7.16,0.76,0.00,0.00,0.00,0.00,0.00,0.00,5.57,2.28,0.00,0.00,0.00,0.00,0.00,2.41,7.54,3.74,2.89,0.08,0.00,0.00,0.00,2.82,4.57,4.57,4.42,0.23],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,3.20,2.28,0.23,0.00,0.00,0.00,0.00,1.98,6.93,5.94,6.55,0.30,0.00,0.00,0.08,6.41,2.37,0.00,5.65,2.68,0.00,0.00,2.13,6.25,0.00,0.00,4.81,2.98,0.00,0.00,1.75,6.71,1.35,0.61,7.04,1.14,0.00,0.00,0.00,3.64,6.94,7.55,3.79,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.08,3.12,4.27,4.57,4.50,1.14,0.00,0.00,0.23,4.42,3.43,3.05,4.95,4.42,0.00,0.00,0.00,0.00,0.15,2.29,6.17,3.73,0.00,0.00,0.00,0.00,4.57,7.62,7.46,0.83,0.00,2.06,2.51,2.29,3.05,3.25,6.93,2.13,0.00,3.28,5.11,5.34,4.73,4.55,2.82,0.15],
[0.00,0.00,2.81,6.02,5.33,0.00,0.00,0.00,0.00,4.29,6.55,2.13,6.86,1.04,0.00,0.00,0.00,7.63,0.53,2.21,7.47,1.52,0.00,0.00,0.00,5.86,5.87,6.15,7.62,1.52,0.00,0.00,0.00,0.15,2.13,2.11,6.25,1.52,0.00,0.00,0.00,0.00,0.00,0.00,6.10,1.52,0.00,0.00,0.00,0.00,0.00,0.00,5.48,1.67,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
]
)

new_labels = model.predict(new_samples)
for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')



