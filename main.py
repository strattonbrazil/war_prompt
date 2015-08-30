import sys

class GameState(object):
    # returns a question and a list of text options
    def getQuestion(self, ctx):
        raise NotImplementedError('getOptions not implemented')

    # gets the new state from the current state, returns None if the
    # game is over
    def advance(self, ctx, choice):
        raise NotImplementedError('advance not implemented')

class GeneralSelectionState(GameState):
    def __init__(self):
        self._options = [
            'General Kane - merciless, but has proven track record',
            'Major Margaret - resourceful and inspiring'
        ]

    def getQuestion(self, ctx):
        return {
            'question' : 'Which general will lead your armies?',
            'options' : self._options
        }
    
    def advance(self, ctx, choice):
        if choice is 1:
            print('General Kane wins the battle')
        elif choice is 2:
            print('Margaret dies very inspiringly')

        return None

class GameContext(object):
    def __init__(self):
        self._state = GeneralSelectionState()

    def printStatus(self):
        questionInfo = self._state.getQuestion(self)

        print(questionInfo['question'])
        print('')
        for i,option in enumerate(questionInfo['options']):
            print('  %i) %s' % (i+1, option))
        print('')

    def handleChoice(self, choice):
        self._state = self._state.advance(self, choice)

        if self._state is None:
            print('\n=== GAME OVER ===\n')
            quit()

if __name__ == "__main__":
    ctx = GameContext()

    # ask questions forever
    while True:
        # print game status
        ctx.printStatus()

        # get next action
        choice = int(raw_input('choice: '))

        ctx.handleChoice(choice)

