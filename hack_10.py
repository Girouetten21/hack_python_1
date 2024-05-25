"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    s = "fooziman"
    s = list(s)
    for i in range(len(s)):
        if s[i] == "o":
            s[i] = "0"
        elif s[i] == "i":
            s[i] = "1"
        elif s[i] == "a":
            s[i] = "@"
    return [c.upper() for c in s]