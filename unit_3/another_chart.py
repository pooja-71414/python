import matplotlib.pyplot as plt
import numpy as np


z1=np.array([50,56,46,45,38,93,46,46])
z2=np.array([54,35,46,88,69,56,57,54])

# plt.plot(z1)
# plt.plot(z2)

# barchart used bar function replace plot function
plt.bar(z1,z2)

# hist() function
# plt.hist(z1)
# plt.hist(z2)

plt.show()