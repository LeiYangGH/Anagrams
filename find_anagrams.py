def read_file_lines(file):
    with open(file, 'r', encoding='utf8', errors='ignore') as f:
        return [l.strip() for l in f.readlines()]

def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)


from collections import defaultdict

def load_words(filename='/usr/share/dict/american-english'):
    with open(filename) as f:
        for word in f:
            yield word.rstrip()

def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        d[key].append(word)
    return d

def print_anagrams(word_source):
    d = get_anagrams(word_source)
    for key, anagrams in d.iteritems():
        if len(anagrams) > 1:
            print(key, anagrams)

word_source = load_words()
print_anagrams(word_source)


from collections import Counter, defaultdict

def anagram(words):
    anagrams = defaultdict(list)
    for word in words:
        histogram = tuple(Counter(word).items()) # build a hashable histogram
        anagrams[histogram].append(word)
    return list(anagrams.values())

keywords = ("hi", "hello", "bye", "helol", "abc", "cab",
                "bac", "silenced", "licensed", "declines")

print(anagram(keywords))




if __name__ == "__main__":
    pass
