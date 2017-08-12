from common import list_files_in_subdirectories_by_extension as list_files
from common import copy_files

# todo build command line interface for this
SOURCE = '/Volumes/BIGMAC/gifs_cropped'
EXTENSION = ''
DEST = '/Volumes/BIGMAC'

files = list_files(SOURCE, EXTENSION)

cor = []
sag = []
tra = []

for f in files:
    if 'masked' not in f:
        if '_cor_' in f:
            cor.append(f)
        if '_sag_' in f:
            sag.append(f)
        if '_tra_' in f:
            tra.append(f)

copy_files(cor, DEST+'/gifs_cropped_cor')
copy_files(sag, DEST+'/gifs_cropped_sag')
copy_files(sag, DEST+'/gifs_cropped_tra')