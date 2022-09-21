#This is for converting all .h5 files in a directory and its sub directories into .fits files within the same folder
import numpy as np
import os
import h5py
from astropy.io import fits
from pathlib import Path

#user to input directory to be searched for .h5 files and convert
print("Enter directory to be converted:")
directory_name = input()

#list of .h5 paths
paths = Path(directory_name).glob('**/*.h5',)

#Find all .h5 files in the directory and its subdirectories
for path in paths:
    f = h5py.File(path, 'r')

    #gets the image data from that file
    image_data = f['image_data'][()]

    #actual conversion
    hdu = fits.PrimaryHDU(image_data)
    hdul = fits.HDUList([hdu])
    
    #create name of converted file using original file name for identification purposes
    name = os.path.splitext(path)[0] + "_converted" + ".fits"
    
    #write to file
    hdul.writeto(name)
    print("converted {}".format(path))


f.close()
