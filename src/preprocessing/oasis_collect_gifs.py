from common import list_files_in_subdirectories_by_extension as list_files
from common import copy_files

# todo build command line interface for this
SOURCE = '/Volumes/BIGMAC'
EXTENSION = '.gif'
DEST = '/Volumes/BIGMAC/gifs'

files = list_files(SOURCE, EXTENSION)
copy_files(files, DEST)