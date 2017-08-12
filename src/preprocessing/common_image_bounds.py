# These imports are actually needed
from common import list_files_in_subdirectories_by_extension as list_files

# These imports are need only for the demo plot
# Uncomment the following two lines for a better windowing experience on mac
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from skimage import io  # used in demo_bounds()

# Global data location variables
SOURCE = '../../data/external_raw/gifs'
DEST = '../../data/in_progress'
EXTENSION = '.gif'


# Returns the bounds of an image inside of which there is actual data
#
# image The scikit-image image to analyze. This can be any 2D array indexed as [y, x]
# left, bottom, right, top The bounds of the image
#  Note: bottom is the lowest y value at which there is data, and top is the highest y value. Typically when displaying
#  an image, low y values are the top and high y values are the bottom, so these bounds may be considered "upside down"
# threshold The integer threshold to use when deciding if a pixel is within the useful bounds of an image
def get_bounds_for_image(image, threshold=0):
    left = len(image)
    right = 0
    top = 0
    bottom = len(image[0])

    for x in range(0, len(image[0])):
        for y in range(0, len(image)):
            if image[y, x] > threshold:
                if x > right:
                    right = x
                if y > top:
                    top = y
                if x < left:
                    left = x
                if y < bottom:
                    bottom = y

    return left, bottom, right, top


# Displays a matplotlib plot of an image surrounded by bounds within which there is data
#
# image The scikit-image image to analyze. This can be any 2D array indexed as [y, x]
def show_plot_with_bounds_for_image(image):
    left, bottom, right, top = get_bounds_for_image(image, threshold=50)

    xy = (left, bottom)
    width = right - left
    height = top - bottom

    plt.imshow(image)

    current_axis = plt.gca()

    current_axis.add_patch(Rectangle(xy, width, height, edgecolor="red", facecolor="none", linewidth=2))

    plt.show()


# Demos the bounds function by applying it to the first image in the SOURCE dataset
def demo_bounds():
    files = list_files(SOURCE, EXTENSION, result_cap=100)
    i = 0
    image = io.imread(files[i])
    plt.figure(i)
    show_plot_with_bounds_for_image(image)


if __name__ == '__main__':
    demo_bounds()
