import operator as op


def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    print("Without Order:", s)
    t = ""
    for i in str:
        if op.countOf(t, i) > 0:
            pass
        else:
            t = t+i
    print("With Order:", t)


str = "geeksforgeeks"
removeDuplicate(str)
