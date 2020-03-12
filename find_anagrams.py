from collections import defaultdict
import datetime


def load_words(filename):
    with open(filename) as f:
        for word in f:
            yield word.strip()


def build_signature_words_dict(words):
    signature_words = defaultdict(list)
    for word in words:
        signature = ''.join(sorted(word))  # if ignore case, use word.lower()
        signature_words[signature].append(word)
    return signature_words


def show_anagrams(signature_words):
    anagrams_lists = [anagrams for anagrams in signature_words.values() if len(anagrams) > 1]
    for anagrams in sorted(anagrams_lists, key=lambda lst: len(lst), reverse=True):
        print(anagrams)


def read_find_show_anagrams(filename='/usr/dict/words'):
    start_time = datetime.datetime.now()
    words = load_words(filename)
    # words = set(words) #if there are duplicates in dictionary
    signature_words = build_signature_words_dict(words)
    show_anagrams(signature_words)
    end_time = datetime.datetime.now()
    print('time used:{}'.format((end_time-start_time).microseconds))


if __name__ == "__main__":
    read_find_show_anagrams(filename='words.txt')
