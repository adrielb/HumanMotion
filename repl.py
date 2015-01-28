import numpy as np
from skimage import data
from skimage.viewer import ImageViewer
from skimage.viewer.plugins.lineprofile import LineProfile

coins = data.coins()
viewer = ImageViewer( coins ) 
viewer.show()

viewer = ImageViewer( coins ) 
viewer += LineProfile(viewer)
overlay, data = viewer.show()[0]

histo = np.histogram( coins, bins=np.arange(0,256) )
histo.show()

from scipy import misc
img = misc.imread('/home/abergman/walking/img/output-00001.png')  

from glob import glob
filelist = glob( '/home/abergman/walking/img/output-*.png' )
filelist.sort()

import matplotlib.pyplot as plt

plt.imshow( img )
plt.show()

type(img)
img.size
img.shape[1]
img.dtype

v = np.arange( 0, img.shape[0] )
u = np.arange( 0, img.shape[1] )
c = np.arange( 0, 3)

tidy = np.asarray([ (v, u, c, img[v,u,c]) 
    for v in range( img.shape[0] )
        for u in range( img.shape[1] )
            for c in range(0,3) ])

tidy = np.asarray([ (v, u, img[v,u,0], img[v,u,1], img[v,u,2] ) 
    for v in range( img.shape[0] )
        for u in range( img.shape[1] )])

tidy.shape

np.savetxt( '/tmp/img.csv', tidy,  delimiter=',', fmt='%d' )
