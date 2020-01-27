class BabbleBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brrok = BabbleBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(brrok)