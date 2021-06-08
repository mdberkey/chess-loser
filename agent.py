# Lichess chess bot designed to lose above all.
import threading

import berserk as bsk

""" Agent of chess game in Lichess"""


class Agent:
    def __init__(self):
        with open('./lichess.token') as tf:
            self.token = tf.read()
        self.session = bsk.TokenSession(self.token)
        self.client = bsk.Client(session=self.session)
        self.client.account.upgrade_to_bot()

    def accept_challenge(self):
        """
        Accepts any lichess challenge and starts the game
        :return: None
        """
        for event in self.client.bots.stream_incoming_events():
            if event['type'] == 'challenge':
                self.client.bots.accept_challenge(event['challenge']['id'])
            elif event['type'] == 'gameStart':
                game = Game(self.client, event['game']['id'])
                game.start()


""" Lichess Game """


class Game(threading.Thread):
    def __init__(self, client, game_id, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.client = client
        self.stream = client.bots.stream_game_state(game_id)
        self.current_state = next(self.stream)

    def run(self):
        """
        Main game loop for bot to read game state and make moves
        :return: None
        """
        self.client.bots.post_message(self.game_id, 'Prepare to win.')
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):
        """
        Evaluates the game state and makes a move
        :param game_state: state of the game
        :return: None
        """
        print(game_state)
        #self.client.bots.make_move(self.game_id, 'e2e4')

    def handle_chat_line(self, chat_line):
        """
        Evaluates the lichess chat and responds depending on chat
        :param chat_line: lichess chat line
        :return: None
        """
        pass


if __name__ == "__main__":
    bot = Agent()
    bot.accept_challenge()
