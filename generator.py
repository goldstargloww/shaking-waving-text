import random

def generate_shake(count = 1, start = 1):
    """
    generates a number of random shake animations in css.
    
    :param int count: the number of shake animations to generate
    :param int start: the number to start at when naming the animations
    :return: the shake animation(s) as a string or list of strings.
    """

    if count <= 0:
        raise ValueError("need at least 1!")
    elif count > 1:
        output = []
        for i in range(count):
            x1 = (random.random()-0.2) * 2
            x2 = (random.random()-0.2) * 2
            x3 = (random.random()-0.2) * 2
            x4 = (random.random()-0.2) * 2
            x5 = (random.random()-0.2) * 2
            x6 = (random.random()-0.2) * 2
            x7 = (random.random()-0.2) * 2
            x8 = (random.random()-0.2) * 2
            x9 = (random.random()-0.2) * 2
            xX = (random.random()-0.2) * 2

            y1 = (random.random()-0.3) * 2
            y2 = (random.random()-0.3) * 2
            y3 = (random.random()-0.3) * 2
            y4 = (random.random()-0.3) * 2
            y5 = (random.random()-0.3) * 2
            y6 = (random.random()-0.3) * 2
            y7 = (random.random()-0.3) * 2
            y8 = (random.random()-0.3) * 2
            y9 = (random.random()-0.3) * 2
            yX = (random.random()-0.3) * 2
            output.append("@keyframes shake" + str(i + start) + " {\n  0%   { transform: translate(" + str(x1) + "px, " + str(y1) + "px)}\n  10%  { transform: translate(" + str(x2) + "px, " + str(y2) + "px)}\n  20%  { transform: translate(" + str(x3) + "px, " + str(y3) + "px)}\n  30%  { transform: translate(" + str(x4) + "px, " + str(y4) + "px)}\n  40%  { transform: translate(" + str(x5) + "px, " + str(y5) + "px)}\n  50%  { transform: translate(" + str(x6) + "px, " + str(y6) + "px)}\n  60%  { transform: translate(" + str(x7) + "px, " + str(y7) + "px)}\n  70%  { transform: translate(" + str(x8) + "px, " + str(y8) + "px)}\n  80%  { transform: translate(" + str(x9) + "px, " + str(y9) + "px)}\n  90%  { transform: translate(" + str(xX) + "px, " + str(yX) + "px)}\n  100% { transform: translate(" + str(x1) + "px, " + str(y1) + ")}\n}")
        return output
    elif count == 1:
        x1 = (random.random()-0.2) * 2
        x2 = (random.random()-0.2) * 2
        x3 = (random.random()-0.2) * 2
        x4 = (random.random()-0.2) * 2
        x5 = (random.random()-0.2) * 2
        x6 = (random.random()-0.2) * 2
        x7 = (random.random()-0.2) * 2
        x8 = (random.random()-0.2) * 2
        x9 = (random.random()-0.2) * 2
        xX = (random.random()-0.2) * 2

        y1 = (random.random()-0.3) * 2
        y2 = (random.random()-0.3) * 2
        y3 = (random.random()-0.3) * 2
        y4 = (random.random()-0.3) * 2
        y5 = (random.random()-0.3) * 2
        y6 = (random.random()-0.3) * 2
        y7 = (random.random()-0.3) * 2
        y8 = (random.random()-0.3) * 2
        y9 = (random.random()-0.3) * 2
        yX = (random.random()-0.3) * 2
        return "@keyframes shake" + str(start) + " {\n  0%   { transform: translate(" + str(x1) + "px, " + str(y1) + "px)}\n  10%  { transform: translate(" + str(x2) + "px, " + str(y2) + "px)}\n  20%  { transform: translate(" + str(x3) + "px, " + str(y3) + "px)}\n  30%  { transform: translate(" + str(x4) + "px, " + str(y4) + "px)}\n  40%  { transform: translate(" + str(x5) + "px, " + str(y5) + "px)}\n  50%  { transform: translate(" + str(x6) + "px, " + str(y6) + "px)}\n  60%  { transform: translate(" + str(x7) + "px, " + str(y7) + "px)}\n  70%  { transform: translate(" + str(x8) + "px, " + str(y8) + "px)}\n  80%  { transform: translate(" + str(x9) + "px, " + str(y9) + "px)}\n  90%  { transform: translate(" + str(xX) + "px, " + str(yX) + "px)}\n  100% { transform: translate(" + str(x1) + "px, " + str(y1) + ")}\n}"
    else:
        raise Exception("what")

def wrap_in_spans(input: str):
    output = ""
    for i in input:
        if i == " ":
            output += " "
        else:
            output += "<span>" + i + "</span>"
    return output

def wrap_in_spans_with_spaces(input: str):
    output = ""
    for i in input:
        if i == " ":
            output += "<span>&nbsp;</span>"
        else:
            output += "<span>" + i + "</span>"
    return output

print(wrap_in_spans("here's some text wrapped in spans"))
print(wrap_in_spans_with_spaces("alright now here's some waving text. you can change the wavelength in the css :> this is also painful on the literally every character has a span front but it's fiiiine"))