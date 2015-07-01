import Quartz


class Writer:
    def __init__(self):
        pass


    def keypress(self, letters):
        for letter in letters:
            event = Quartz.CGEventCreateKeyboardEvent(None, 0, True)
            Quartz.CGEventKeyboardSetUnicodeString(event, 1, letter)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)