class BotPlayer:
    def __init__(self):
        self.all_words = get_all_words()
        self.poss_words = []
        self.cur_letters = []
        self.points = {
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

    def set_cur_letters(self, new_letters):
        self.cur_letters = new_letters
        self.get_poss_words()
        print("current letters and possible words set")

    def get_start_word(self):
        max_eff = 0
        max_word = []
        for word in self.poss_words:
            score = get_points(self.points, word)
            eff = score / len(word)
            if eff > max_eff and len(word) > 3:
                max_eff = eff
                max_word = [word]
            elif eff == max_eff:
                max_word.append(word)
        return max_word

    def get_poss_words(self):
        for word in self.all_words:
            if check_word(self.cur_letters, word):
                self.poss_words.append(word)


def get_all_words():
    with open("filteredWords.txt", "r") as f:
        return [row.strip() for row in f.readlines() if row.strip() != ""]


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


def main():
    bot = BotPlayer()
    bot.set_cur_letters(['o', 'r', 'g', 'e', 'd', 'i', 'n', 'n', 'g', 'o', 'h', 'f', 'l'])
    print(bot.cur_letters)
    print(bot.get_start_word())


if __name__ == "__main__":
    main()