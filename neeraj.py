#File to compute the angle between two
#text files

import math
import string
import sys

def read_file(filename):
    try:
        file_name_opened = open(filename)
        line_read_from_file = file_name_opened.readlines()
    except IOError:
        print "Error opening or reading the input file:", filename
        sys.exit()
    return line_read_from_file

def get_words_from_line_list(line_read_file):
    word_list = []
    for line in line_read_file:
        words_in_line = get_words_from_string(line)
        word_list = word_list + words_in_line
    return word_list

def get_words_from_string(line):
    word_list = []
    character_list = []
    for counter_1 in line:
        if counter_1.isalnum():
            character_list.append(counter_1)
        elif len(character_list) > 0:
            word = string.join(character_list, "")
            word = string.lower(word)
            word_list.append(word)
            character_list = []

    if len(character_list) > 0:
        word = string.join(character_list, "")
        word = string.lower(word)
        word_list.append(word)
    return word_list

def count_frequency(word_list1):
    line_tobe_read = []
    #print line_tobe_read
    for new_word in word_list1:
       # print new_word
        for entry in line_tobe_read:
            if new_word == entry[0]:
                entry[1] = entry[1]+1
                break
        else:
            line_tobe_read.append([new_word, 1])
    return line_tobe_read


def insertion_sort(line_sort):
    for j in range(len(line_sort)):
        key = line_sort[j]
        i = j-1
        while i > -1 and line_sort[i] > key:
            line_sort[i+1] = line_sort[i]
            i = i-1
        line_sort[i+1] = key
    return line_sort

def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    insertion_sort(freq_mapping)

    print "File", filename, ":",
    print len(line_list), "lines,",
    print len(word_list), "words,",
    print len(freq_mapping), "distinct words"

    return freq_mapping

def inner_product(line_1, line_2):
    sum_1 = 0.0
    i = 0
    j = 0
    while i < len(line_1) and j < len(line_2):
        # L1[i:] and L2[j:] yet to be processed
        if line_1[i][0] == line_2[j][0]:
            # both vectors have this word
            sum_1 += line_1[i][1] * line_2[j][1]
            i += 1
            j += 1
        elif line_1[i][0] < line_2[j][0]:
            # word L1[i][0] is in L1 but not L2
            i += 1
        else:
            # word L2[j][0] is in L2 but not L1
            j += 1
    return sum_1

def vector_angle(line_angle1, line_angle2):
    """
    Return the angle between these two vectors.
    """
    numerator = inner_product(line_angle1, line_angle2)
    denominator = math.sqrt(inner_product(line_angle1, line_angle1)*inner_product(line_angle2, line_angle2))
    return math.acos(numerator/denominator)

def main():
    if len(sys.argv) != 3:
        print "Usage: docdist1.py filename_1 filename_2"
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
        print "The distance between the documents is: %0.6f (radians)"%distance


if __name__ == "__main__":
    main()
