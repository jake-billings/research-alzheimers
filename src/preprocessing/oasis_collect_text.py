from common import copy_files
from common import list_files_in_subdirectories_by_extension as list_files


# This Script will find all .txt files in folders of the data and store them in the external_raw folder

# Insure that the Source only points to the folder that has Disk files with the PAT records in them
SOURCE = '/Users/gunnarenserro/Desktop/Oasis_data/'
EXSTENSION = '.txt'
DEST = '../../data/external_raw/Pat_data'


files = list_files(SOURCE, EXSTENSION)
if len(files) % 2 == 1:
    raise ValueError('Does not have correct amount of files!')

copy_files(files[0::2], DEST)


