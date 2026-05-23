from Crypto.Util.number import *
import sys
sys.setrecursionlimit(1000000)

_ = bytes_to_long(
    b'why_would_someone_write_math_like_this_anyway'
)

__ = bytes_to_long(
    b'this_recursion_depth_is_absolutely_unnecessary'
)

def _____(_,__,___):
    if _ == 0 or __ == 0:
        return 0

    if _ == 1 and __ == 1:
        return 1

    if __ == 1:
        return (_ + 1 + _____(_-1,__,___) + _____(_,__-1,___)) // 2

    if ___ == 0:
        return _ + _____(_,__-1,___)

    return 1 + _____(_ + __, _____(_,__,___-1) - 1, ___-1) // (_ + __)

enc = 11551380463205030145984505292544417183760060160345830286767849206745608764828130208228640898099483848539678213765996211325950437007166303077649440473541712588330646109097201709975224837143082992695224313116018965

print(enc)
