from skimage.transform import resize
from skimage import io
from common import list_files_in_subdirectories_by_extension as list_files
from numpy import mean
from numpy import std
from math import floor
import matplotlib.pyplot as plt

SOURCES = ['../../data/external_raw/gifs_cropped_cor',
           '../../data/external_raw/gifs_cropped_sag',
           '../../data/external_raw/gifs_cropped_tra']
DESTS = ['../../data/external_raw/gifs_cropped_cor_scaled',
         '../../data/external_raw/gifs_cropped_sag_scaled',
         '../../data/external_raw/gifs_cropped_tra_scaled']
EXTENSION = ''
SAVE_FORMAT = 'PNG'

for SOURCE, DEST in zip(SOURCES, DESTS):
    files = list_files(SOURCE, EXTENSION, result_cap=1000)

    heights = []
    widths = []

    for f in files:
        img = io.imread(f)
        heights.append(len(img))
        widths.append(len(img[0]))

        widths = sorted(widths)
        heights = sorted(heights)

    print 'Width: mean: ', mean(widths), 'std', std(widths)
    print 'Height: mean: ', mean(heights), 'std', std(heights)

    new_width = floor(mean(widths))
    new_height = floor(mean(heights))

    for f in files:
        img = io.imread(f)
        save_path = f.replace(SOURCE, DEST)

        resized_image = resize(img, (new_width, new_height))
        plt.imsave(save_path, resized_image, cmap=plt.cm.gray, format=SAVE_FORMAT)