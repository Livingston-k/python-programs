from skpy import SkypeEventLoop, SkypeNewMessageEvent

class SkypePing(SkypeEventLoop):
    def __init__(self):
        super(SkypePing, self).__init__('yourskypeusername/email', 'your skype password')
        print("actively waiting for messages")
    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent) \
          and not event.msg.userId == self.userId :
          # sending automated reply
          event.msg.chat.sendMsg("Hi there, Kaddu Livingston is currently out call on 256701512709")

sk = SkypePing()
sk.loop()

inp = input('end:')