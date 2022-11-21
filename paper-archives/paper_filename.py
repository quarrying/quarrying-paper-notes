import os
import khandy


stop_words = ['and', 'as', 'at', 'by', 'for', 'from', 'in', 'of', 'on', 'or', 
              'the', 'to', 'via','with',]


def is_capitalized(filename):
    stem = khandy.get_path_stem(filename)
    parts = stem.split()
    for item in parts:
        if not item[0].isalpha():
            continue
        if not item[0].isupper() and item not in stop_words:
            return False
    return True
    

if __name__ == '__main__':
    records = khandy.load_list('archives/202203.txt')
    for record in records:
        if not is_capitalized(record):
            print(record)
