# Module-required imports
from common import list_files_in_subdirectories_by_extension as list_files
from common_image_bounds import get_bounds_for_image
from skimage import io

# Demo-required imports
import matplotlib.pyplot as plt

# todo build command line interface for this
SOURCE = '../../data/external_raw/gifs'
EXTENSION = '.gif'
DEST = '../../data/external_raw/gifs_cropped'
SAVE_FORMAT = 'png'
SAVE_EXTENSION = '.' + SAVE_FORMAT
THRESHOLD = 50


# Loads image from a path and returns a cropped scikit-image (2D matrix indexed [y, x])
# that is cropped to the area that contains data
#
# path The path of the image to read and crop
def load_and_crop_image(path):
    # Read the image data
    image = io.imread(path)

    # Calculate the bounds
    left, bottom, right, top = get_bounds_for_image(image, threshold=THRESHOLD)

    # Crop the image
    cropped_image = image[bottom:top, left:right]

    # Return the image
    return cropped_image


# Crops all images in the OAISIS data set based on the global SOURCE and DEST parameters
def crop_oaisis_images():
    # Get the list of files from the source data
    files = list_files(SOURCE, EXTENSION)

    # Iterate over each file path
    for f in files:

        # Load and crop the image at path f
        cropped_image = load_and_crop_image(f)

        # Assign a path for saving. We need to move it from source to dest,
        # so do some path replacement
        save_path = f.replace(SOURCE, DEST).replace(EXTENSION, SAVE_EXTENSION)

        # Save the new cropped image
        plt.imsave(save_path, cropped_image, cmap=plt.cm.gray, format=SAVE_FORMAT)


# Crops all images in the OAISIS data set based on the global SOURCE and DEST parameters
def demo_plot_cropped_image():
    # Get the list of files from the source data
    files = list_files(SOURCE, EXTENSION,result_cap=1)

    # Crop the first image
    cropped_image = load_and_crop_image(files[0])

    # Plot the image using matplotlib
    plt.imshow(cropped_image)
    plt.show()


if __name__ == '__main__':
    crop_oaisis_images()