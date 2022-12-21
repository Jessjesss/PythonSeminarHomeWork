from bisect import bisect_left

def search_data(record, wordtofind):

    words = []
    for line in record:
        words.extend(line.strip().split(','))
    ind = bisect_left(words,wordtofind)
    if words[ind] == wordtofind:
    print ('%s was found!' % wordtofind)