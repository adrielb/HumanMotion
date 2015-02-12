import sys
import numpy as np
from skimage.segmentation import slic
from skimage.util import img_as_float
from scipy import misc

inputfile=sys.argv[1]
outputfile=sys.argv[2]
seg_init=20
compactness=5
sigma=2

img = misc.imread(inputfile)  

n_segs=np.prod( np.array(img.shape)[0:2] / seg_init )

segments = slic( img, n_segments=n_segs, compactness=compactness, sigma=sigma)

np.save( outputfile, segments)
