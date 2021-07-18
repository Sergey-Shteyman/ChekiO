from datetime import datetime


def days_diff(a, b):
    return abs((datetime(*a) - datetime(*b)).days)


print(days_diff((1982, 4, 19), (1982, 4, 22)))