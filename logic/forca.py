class Forca:
    word: str
    lives: int

    guessed_chars = []

    def verify(self):
        for c in self.word:
            if c not in self.guessed_chars:
                return False
        return True

    def guess(self, char):
        if char in self.word:
            self.guessed_chars.append(char)
            return True
        else:
            self.lives -= 1
            return False


    def __init__(self, word, lives):
        self.word, self.lives = word, lives
