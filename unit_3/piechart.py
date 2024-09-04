import matplotlib.pyplot as plt

s=[4,5,20,16]
stream=['neural network','machine learning','cloud computing','AI/TOC']
col=['r','g','b','cyan']
exp=[0.1,0,0,0]
plt.pie(s,labels=stream,colors=col,shadow=True,explode=exp)
plt.show()