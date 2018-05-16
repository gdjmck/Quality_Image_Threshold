import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import data, img_as_float, color 
from skimage.util import random_noise


#original = img_as_float(data.chelsea()[100:250, 50:300])
original = io.imread('--------enter path to images ----------')


sigma = 0.155
noisy = random_noise(original, var=sigma**2)

# Estimate the average noise standard deviation across color channels.
sigma_est = estimate_sigma(noisy, multichannel=True, average_sigmas=True)

# Due to clipping in random_noise, the estimate will be a bit smaller than the
# specified sigma.
print("Estimated Gaussian noise standard deviation = {}".format(sigma_est))


