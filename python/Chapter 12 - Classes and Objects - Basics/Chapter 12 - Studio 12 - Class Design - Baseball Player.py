#  A baseball player has a name and a jersey number. Most players hit either
#  right or left, but some can hit either way. This object should be able
#  to react when a player completes a game, recording how many hits and RBIs
#  the player earned in that game. A player has a certain number of runs and
#  RBIs he or she has recorded over all games played. A player has a certain
#  number of games he or she has played.


class Baseball_player():

    def __init__(self, name, jersey_number, batting_pref):
        self.name = name
        self.jersey_number = jersey_number
        self.batting_pref = batting_pref
        self.total_games = 0
        self.total_hits = 0
        self.total_runs = 0
        self.total_rbis = 0

    def game_stats(self, hits, runs, rbis):
        self.total_games += 1
        self.total_hits += hits
        self.total_runs += runs
        self.total_rbis += rbis

    def __repr__(self):
        __repr = '{"_Baseball_player__name": "' + \
                 str(self.name) + '",' + \
                 ' "_Baseball_player__jersey_number": ' + \
                 str(self.jersey_number) + \
                 ' "_Baseball_player__batting_pref": "' + \
                 str(self.batting_pref) + '",' + \
                 ' "_Baseball_player__total_games": ' + \
                 str(self.total_games) + ',' + \
                 ' "_Baseball_player__total_hits": ' + \
                 str(self.total_hits) + ',' + \
                 ' "_Baseball_player__total_runs": ' + \
                 str(self.total_runs) + ',' + \
                 ' "_Baseball_player__total_rbis": ' + \
                 str(self.total_rbis) + \
                 '}'
        return __repr


def my_test_equal(a, b):
    """ Home-rolled version of testEqual(a, b) """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of Baseball_player Class """

    bp1 = Baseball_player("Carl Yastremski", 4, "left")
    bp2 = Baseball_player("Benny Switcheroo", 45, "switch")
    print(bp1)
    print(bp2)
    bp2.game_stats(3, 1, 1)
    bp2.game_stats(1, 0, 0)
    bp2.game_stats(0, 1, 0)
    print(bp2)


if __name__ == "__main__":
    main()
