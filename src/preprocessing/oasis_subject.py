import csv


# Simple class to represent the patient information found in the OASIS csv file
class Subject:
    def __init__(self, identifier, sex, hand, age, educ, ses, mmse, cdr, etiv, nwbv, asf, delay):
        self.identifier = identifier
        self.sex = sex
        self.hand = hand
        self.age = age
        self.educ = educ
        self.ses = ses
        self.mmse = mmse
        self.cdr = cdr
        self.etiv = etiv
        self.nwbv = nwbv
        self.asf = asf
        self.delay = delay

    def __repr__(self):
        return '%s: %s year old %s with %s cdr' % (self.identifier, self.age, self.sex, self.cdr)


# Deserialize a subject from to row in the provided OASIS csv file
#
# subject - A subject object to export to the csv row array
def serialize_subject_to_csv_row_array(subject):
    row = []

    row.append(subject.identifier)
    row.append(subject.sex)
    row.append(subject.hand)
    row.append(subject.age)
    row.append(subject.educ)
    row.append(subject.ses)
    row.append(subject.mmse)
    row.append(subject.cdr)
    row.append(subject.etiv)
    row.append(subject.nwbv)
    row.append(subject.asf)
    row.append(subject.delay)

    return row


# Deserialize a subject from a row in the provided OASIS csv file
#
# row - A row from the OASIS patient data CSV file
def deserialize_subject_from_csv_row_array(row):
    cdr = 0
    if row[7] != '':
        cdr = float(row[7])
    subject = Subject(row[0], row[1], row[2],
                      float(row[3]), row[4], row[5],
                      row[6], cdr, row[8],
                      row[9], row[10], row[11])

    return subject


# Deserialize multiple subjects from a 2D array representing the provided OASIS csv file
#
# rows - a 2D array representing the provided OASIS csv file from the csv library
def deserialize_bulk_from_csv_array(rows):
    subjects = []
    for row in rows:
        subjects.append(deserialize_subject_from_csv_row_array(row))
    return subjects


# Deserialize multiple subjects from the provided OASIS csv file found at the path 'source'
#
# source - the path to the provided OASIS csv file
def deserialize_bulk_from_csv_file(source):
    with open(source, 'rb') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_rows = []
        for row in csv_reader:
            csv_rows.append(row)
        return deserialize_bulk_from_csv_array(csv_rows[1:])
