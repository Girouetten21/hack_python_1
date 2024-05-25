"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    s = "fooziman"
    s = s.replace("o", "0")
    s = s.replace("i", "1")
    s = s.replace("a", "@")
    return s