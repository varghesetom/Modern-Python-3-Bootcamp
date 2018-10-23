from random import choice

def eat(food, is_healthy):
    ending = "I don't care about my health"
    if is_healthy:
        ending = "because my body is a temple"
    return "I'm eating {0}, {1}".format(food, ending)
