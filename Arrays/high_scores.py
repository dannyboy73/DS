class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class Scoreboard:
    """Fixed-length sequence of high scores in ascending order"""

    def __init__(self, capacity=10):
        """All entries are None"""
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        """Entry at index k"""
        return self._board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()

        # does new entry qualify as a high score?
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry

            self._board[j] = entry

ge1 = GameEntry('Mike', 1105)
ge2 = GameEntry('Rob', 750)
ge3 = GameEntry('Paul', 720)
ge4 = GameEntry('Anna', 660)
ge5 = GameEntry('Rose', 590)
ge6 = GameEntry('Jack', 510)
ge7 = GameEntry('Jill', 740)

score_board = Scoreboard()
score_board.add(ge1)
score_board.add(ge2)
score_board.add(ge3)
score_board.add(ge4)
score_board.add(ge5)
score_board.add(ge6)
score_board.add(ge7)
print(score_board)
