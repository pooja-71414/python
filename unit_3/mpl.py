import matplotlib.pyplot as plt
import numpy as np

# x=np.array([0,5])
# y=np.array([0,100])
# plt.plot(x,y)

# z1=np.array([50,56,46,45,38,93,46,46])
# z2=np.array([54,35,46,88,69,56,57,54])
# plt.plot(z1)
# plt.plot(z2)

z1=np.array([50,56,46,45,38,93,46,46])
z2=np.array([54,35,46,88,69,56,57,54])
# properties of plot() function
# marker values=D,P,o,v,s
# color values=rgb-combination
# linestyle values=dashed,solid....
# linewidth values=1,2,3,4,5,6.........
# markersize or ms values=1,2,3............
# mec(marker eage color) values=r,g,b,rgb-combination

# properties of xlabel(),ylabel(),title() function
# fontdict=dictionary_name           
# create font-dictionary
# font={'family':'Arial','size':10,'color':'red'}

# plt.grid() property
# linewidth values=1,2,3,4,5.......
# color values=colorname
plt.grid(linewidth='0.5',color='purple') 

fontforxlabel={'family':'Arial','size':20,'color':'red'}
fontforylabel={'family':'Arial Rounded MT Bold','size':30,'color':'blue'}
fontfortitle={'family':'Algerian','size':40,'color':'pink'}
plt.xlabel('X-axes',fontdict=fontforxlabel)
plt.ylabel('Y-axes',fontdict=fontforylabel)
plt.title('Title',fontdict=fontfortitle)

plt.plot(z1,marker='D',color='r',linestyle='dashed',linewidth='1',markersize='5',mec='b')
plt.plot(z2,marker='o',color='g',linestyle='solid',linewidth='2',markersize='10',mec='b')

plt.show()