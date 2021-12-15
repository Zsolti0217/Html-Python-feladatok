import sys

def teszt(tesztEset):
    sorszam = sys._getframe(1).f_lineno # visszaadja a hívó sorának számát
    if tesztEset:
        msg = "A(z) {0}. sorban álló sikeres.".format(sorszam)
    else :
        msg = "A(z) {0}. sorban álló SIKERTELEN.".format(sorszam)
    print(msg)