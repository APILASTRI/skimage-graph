import graph
import time
import sys
import tiffile as tf
from skimage import io
from matplotlib import pyplot as plt
import numpy as np
import random
from skimage.morphology import watershed
from scipy.ndimage import label
from scipy.ndimage.filters import gaussian_filter as gf
from skimage.util import img_as_float

threshold = 0.005
sigma = 1
img = tf.imread('../data/image.tif')
boundary = tf.imread('../data/prob.tif')

boundary = boundary.astype(np.float32)/255
boundary = gf(boundary, sigma)


seed_mask = boundary < 0.01
seed_label, n = label(seed_mask)
del seed_mask
del boundary

print "Found %d Seeds" % n
w = watershed(img, seed_label)
np.save("watershed",w)
