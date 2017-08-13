# Script is meant for collecting the text in the external_raw file, then putting it into a
# more readable format for the computer, they had xml but it was strange to try and parse and
# way easier to just parse the text files

SOURCE = '../../data/external_raw/Pat_data'

# dirr will be the directory to the folders of disk


def load_data(pat_id):
    try:
        f = open(SOURCE + ('/OAS1_{}_MR1.txt'.format('%04d' % pat_id)), 'r')
    except IOError:
        print("ID is not in records")
        return

    data = []
    num_blank = 0
    for line in f.readlines():
        a = line.split(':')
        if len(a) != 1:
            data.append((a[0].lower(), a[1].strip()))
        elif num_blank != 2:
            num_blank += 1
        else:
            return dict(data)

    return dict(data)


if __name__ == '__main__':
    print(load_data(1))

