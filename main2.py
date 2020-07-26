def get_all_words():
    with open("filteredWords.txt", "r") as f:
        return [row.strip() for row in f.readlines() if row.strip() != ""]


def get_points(points, word):
    total = 0
    for ch in word:
        total += points[ch]
    return total


class BotPlayer:
    def __init__(self):
        self.all_words = get_all_words()
        self.cur_letters = []
        self.cur_letters_left = []
        self.poss_words = []
        self.starting_words = []
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

    def set_poss_words(self):
        for word in self.all_words:
            good = True
            temp = list(self.cur_letters)
            for ch in word:
                if ch in temp:
                    temp.remove(ch)
                else:
                    good = False
                    pass
            if good:
                self.poss_words.append(word)

    def set_cur_letters(self, new_letters):
        self.cur_letters = new_letters.split()
        self.set_poss_words()

    def get_start_word(self):
        max_eff = 0
        max_word = []
        for word in self.poss_words:
            score = get_points(self.points, word)
            eff = score / len(word)
            if eff > max_eff and len(word) > 3 and score > 10:
                max_eff = eff
                max_word = [[word, eff, score]]
            elif eff == max_eff and score > 10:
                max_word.append([word, eff, score])
        self.starting_words = max_word
        return max_word


def main():
    bot = BotPlayer()
    bot.set_cur_letters('o p y e d i n n e o h f l')
    for item in bot.get_start_word():
        print(item)


if __name__ == "__main__":
    main()
