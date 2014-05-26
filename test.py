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
from scipy.ndimage.measurements import watershed_ift

slice = 200
img = tf.imread('../data/image.tif')
boundary = tf.imread('../data/prob.tif')

boundary = img_as_float(boundary)
boundary = gf(boundary,5)
raw_input("Enter")


seed_mask = boundary < 0.01
seed_label,n = label(seed_mask)

print "Found %d Seeds" % n
w = watershed(img, seed_label)

