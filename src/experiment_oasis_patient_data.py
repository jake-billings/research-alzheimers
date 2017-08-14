from numpy import mean
from numpy import std
from matplotlib import pyplot as plt
from scipy.stats import norm
from preprocessing.oasis_subject import deserialize_bulk_from_csv_file

INDEX_SOURCE = '../../data/external_raw/csv/oasis_cross-sectional.csv'

subjects = deserialize_bulk_from_csv_file(INDEX_SOURCE)

rv = norm()


def draw_plot_for_freq_data(name, data, fig, subplot, _min, _max, overscan=5, step=1, show_normal=True):
    fit = norm.pdf(data, mean(data), std(data))

    xvals = [x * step for x in range(_min, int(_max/step)+1)]

    freq = {}
    for i in xvals:
        freq[i] = 0
    for i in xvals:
        for datum in data:
            if datum == i:
                freq[i] += 1
    for i in xvals:
        freq[i] /= float(len(ages))

    freq_arr = freq.values()

    plt.figure(fig)
    plt.subplot(subplot)
    plt.title(name)

    actual, = plt.plot(xvals, freq_arr, label='Actual Frequencies')
    handles = [actual]

    if show_normal:
        normal, = plt.plot(data, fit, '-o', label='Normal Distribution')
        handles.append(normal)

    plt.xlim([_min - overscan, _max + overscan])
    plt.legend(handles=list(reversed(handles)), bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Age
ages = sorted([subject.age for subject in subjects])
draw_plot_for_freq_data('Ages', ages, 101, 221, int(min(ages)), int(max(ages)))

# CDR
cdrs = sorted([subject.cdr for subject in subjects])
draw_plot_for_freq_data('CDR', cdrs, 101, 223, int(min(cdrs)), int(max(cdrs)), overscan=1, step=0.5)

plt.show()
