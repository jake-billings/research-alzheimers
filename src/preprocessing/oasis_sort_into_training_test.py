from common import list_files_in_subdirectories_by_extension as list_files
from common import copy_files

from oasis_subject import deserialize_bulk_from_csv_file

from random import random

# todo build command line interface for this
INDEX_SOURCE = '../../data/external_raw/csv/oasis_cross-sectional.csv'
SOURCES = ['../../data/external_raw/gifs_cropped_cor_scaled',
           '../../data/external_raw/gifs_cropped_sag_scaled',
           '../../data/external_raw/gifs_cropped_tra_scaled']
DESTS = ['../../data/external_normalized/oasis/cor',
         '../../data/external_normalized/oasis/sag',
         '../../data/external_normalized/oasis/tra']
EXTENSION = ''
AD_THRESHOLD = 0

# This is the 80-20 Training-Test split
# See https://en.wikipedia.org/wiki/Pareto_principle
PROB_ASSIGN_TRAINING = 0.8

# Load the csv file as an array of Python objects (see oasis_subject.py)
subjects = deserialize_bulk_from_csv_file(INDEX_SOURCE)


# Search the subjects array by a patient's identifier
def find_subject_by_identifier(identifier):
    for subject in subjects:
        if identifier == subject.identifier:
            return subject
    raise Exception('Subject not found with identifier %s' % identifier)


for SOURCE, DEST in zip(SOURCES, DESTS):
    files = list_files(SOURCE, EXTENSION)

    positive = []
    negative = []

    positive_training = []
    negative_training = []
    positive_test = []
    negative_test = []

    for f in files:
        subject_identifier = '_'.join(f.split('/')[-1].split('_')[0:3])
        subject = find_subject_by_identifier(subject_identifier)
        subject_has_ad = subject.cdr > AD_THRESHOLD
        if subject_has_ad:
            positive.append(f)
        else:
            negative.append(f)

    for f in positive:
        if random() < PROB_ASSIGN_TRAINING:
            positive_training.append(f)
        else:
            positive_test.append(f)
    for f in negative:
        if random() < PROB_ASSIGN_TRAINING:
            negative_training.append(f)
        else:
            negative_test.append(f)

    copy_files(positive_training, DEST+'/positive/training')
    copy_files(negative_training, DEST+'/negative/training')
    copy_files(positive_test, DEST+'/positive/test')
    copy_files(negative_test, DEST+'/negative/test')
