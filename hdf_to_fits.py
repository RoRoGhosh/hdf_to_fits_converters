#This is for converting singular .h5 files to .fits files
import numpy as np
import os
import h5py
from astropy.io import fits

#file to be converted put here
print("Enter file address to be converted (with .h5 at the end):")
local_data_filename = input()
f = h5py.File(local_data_filename, 'r')

#gets the image data from that file
image_data = f['image_data'][()]

#actual conversion
hdu = fits.PrimaryHDU(image_data)
hdul = fits.HDUList([hdu])

#writes to file name
print("Enter new file name (with .fits at the end):")
name = input()
hdul.writeto(name)

f.close()
