import sys

def test(n):
    j = 0
    for i in range(n):
        j = j + i
    return n

def profiler(frame, event, arg):
    print(event, frame.f_code.co_name, frame.f_lineno, "->", arg)
# profiler is activated on the next call, return, or exception
sys.setprofile(profiler)
# profile this function call/
test(1)