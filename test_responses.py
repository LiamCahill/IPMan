import random
import responses


def test_responses():
    assert responses.get_response("hello") == "Go away!"

    min_range=0
    max_range=6
    # I just want to check if the value returned here is an int within the range 0-6.
    #assert responses.get_response("roll") ==
    assert responses.get_response("!help") == "`This is a help message that you can modify.`"
    assert responses.get_response("unhandled message") == 'I didn\'t understand what you wrote. Try typing "!help"'
