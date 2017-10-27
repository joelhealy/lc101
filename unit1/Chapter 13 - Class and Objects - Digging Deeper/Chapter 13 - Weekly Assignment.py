#  Your job is to make a subclass called BoredChatbot that inherits from
#  Chatbot, but acts a little differently, in the following way:
#
#     A bored chatbot has a short attention span. When the human says something
#     that is longer than 20 characters, it should respond by saying:
#
#          “zzz... Oh excuse me, I dozed off reading your essay.”
#
#     If, on the other hand, the human says something with a length of 20
#     characters or less, then the bored chatbot should respond just like a
#     normal chatbot would.
#
#  Note that we are requiring you to use inheritance. Your new BoredChatbot
#  class must be a subclass of the Chatbot class, and your subclass should only
#  implement the things that make it distinct. (See the Inheritance chapter
#  for a review of how this works.)


class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + \
            prompt_from_human + "'"


class BoredChatbot(Chatbot):
    """ A surly version of Chatbot to show I can create a subclass """

    def response(self, prompt_from_human):
        """ Returns the BoredChatbot's response to something the human said """
        if len(prompt_from_human) > 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return Chatbot.response(self, prompt_from_human)


def my_test_equal(a, b):
    """ Home-rolled version of testEqual(a, b) """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of BoredChatbot class """

    my_test_equal(BoredChatbot("Ralph").response("Chow"),
                  "It is very interesting that you say: 'Chow'")
    my_test_equal(BoredChatbot("Norton").response("123456789012345678901"),
                  "zzz... Oh excuse me, I dozed off reading your essay.")


if __name__ == "__main__":
    main()
