import string
import re
import sys


def open_file(name):
    with open(name, "r") as f:
        return [row.strip() for row in f.readlines() if row.strip() != ""]


def filter_words(words):
    return [word for word in words
            if not any(ch in string.digits + " " + string.punctuation for ch in word)
            and 1 < len(word) < 14]


def get_abbr():
    result = []
    with open("wikiStuff.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if re.search(" .+ ?\|\|", line):
                m = re.search("\}? .+ ?\|\|", line).group(0)[0:-2]\
                    .upper().replace(".", "")\
                    .replace("[[", "") \
                    .replace("]]", "")\
                    .strip()
                if "}}" in m:
                    m = m.split("}}")[-1].strip()
                # if len(m) > 6:
                #     print(m)
                if " OF " in m:
                    m = m.split(" OF ")[-1]
                if "|" in m:
                    m = m.split("|")[-1]
                if "/" in m:
                    m = m.split(" / ")[-1].strip()
                if not any(ch in string.punctuation for ch in m) and len(m) < 10:
                    result.append(m)
    return result


def write_to_file(words):
    with open("filteredWords.txt", "w", encoding="utf-8") as f:
        for word in words:
            print(word, file=f)


def remove_abbr(words):
    abbr = get_abbr()
    i = 0
    for word in words:
        words[i] = word.lower()
        if word.upper() in abbr:
            words.pop(i)
        i += 1
    return sorted(set(words))


def print_frame():
    for i in range(0, 13):
        print("{0}".format(" | q | "*13))
        print()


def check_word(letters, word):
    possible = True
    for ch in word:
        if ch not in letters:
            possible = False
        else:
            letters.remove(ch)
    return possible


def get_points(points, word):
    total = 0
    for ch in word:
        total += points[ch]
    return total


def get_start_word(points, words):
    pass


def main(argv):
    # create word list
    # write_to_file(remove_abbr(filter_words(open_file("words.txt"))))

    words = open_file("filteredWords.txt")
    points = {
        "a": 1,
        "b": 3,
        "c": 2,
        "d": 1,
        "e": 1,
        "f": 3,
        "g": 2,
        "h": 2,
        "i": 1,
        "j": 5,
        "k": 3,
        "l": 2,
        "m": 3,
        "n": 1,
        "o": 2,
        "p": 4,
        "q": 7,
        "r": 1,
        "s": 1,
        "t": 2,
        "u": 2,
        "v": 4,
        "w": 3,
        "x": 6,
        "y": 7,
        "z": 5
    }
    # print_frame()
    pos_words = []
    max_score = 0
    max_word = ""
    max_eff = 0
    best_start_word = ""
    for word in words:
        if check_word(argv[1].split(), word):
            pos_words.append(word)
    for word in pos_words:
        score = get_points(points, word)
        print("{0:13}{1:<6}{2}".format(word, score, score/len(word)))
        if score > max_score:
            max_score = score
            max_word = word
        if score/len(word) > max_eff and len(word) > 3:
            max_eff = score/len(word)
            best_start_word = word
    print(max_score, max_word)
    print(max_eff, best_start_word)


if __name__ == "__main__":
    main(sys.argv)
