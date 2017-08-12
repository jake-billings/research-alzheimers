from scipy.stats import norm
from skimage import io
from preprocessing.common import list_files_in_subdirectories_by_extension as list_files
from numpy import mean
from numpy import std
from numpy import unique
import pylab as plt

SOURCE_RAW = '../../data/external_raw/gifs'
SOURCE_CROPPED = '../../data/external_raw/gifs_cropped'
EXTENSION = ''

rv = norm()

files = list_files(SOURCE_CROPPED, EXTENSION, result_cap=1000)

heights = []
widths = []

img_a = 0
img_b = 47

i = 0

plt.figure(8)

for f in files:
    img = io.imread(f)
    heights.append(len(img))
    widths.append(len(img[0]))

    if i == img_a:
        plt.subplot(223)
        plt.title('Image A')
        plt.imshow(img)

    if i == img_b:
        plt.subplot(224)
        plt.title('Image B')
        plt.imshow(img)

    i += 1

widths = sorted(widths)
heights = sorted(heights)

# result = norm.pdf(range(0, 100), loc = 50, scale = 50)
width_fit = norm.pdf(widths, mean(widths), std(widths))
height_fit = norm.pdf(heights, mean(heights), std(heights))

print unique(widths)
print unique(heights)

print 'Mean width', mean(widths)
print 'Mean height', mean(heights)

plt.subplot(221)
plt.title('Widths')
plt.plot(widths,width_fit,'-o')

plt.subplot(222)
plt.title('Heights')
plt.plot(heights,height_fit,'-o')

plt.show()