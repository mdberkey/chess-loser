# Lichess chess bot designed to lose above all.
import berserk as bsk

""" Agent of chess game in Lichess"""


class Agent:
    def __init__(self):
        with open('./lichess.token') as tf:
            self.token = tf.read()

    def start(self):
        print(self.token)
        #session = bsk.TokenSession(self.token)
        #client = bsk.Client(session=session)

if __name__ == "__main__":
    bot = Agent()
    bot.start()