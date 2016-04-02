from yoda_speak import yoda

def test_yoda_speak_happy():
    print yoda("Hi, whats up?")

def test_yoda_speak_love():
    print yoda("May the force be with you")

def test_yoda_speak_negative():
    print yoda("#$%#$%!")

if __name__ == '__main__':
    test_yoda_speak_happy()
    test_yoda_speak_love()
    test_yoda_speak_negative()
