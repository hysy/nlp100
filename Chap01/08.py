def chiper(s):
    ret = ""
    for c in s:
        n = ord(c)
        if c.lower() :
            ret += chr(219 - n)
        else :
            ret += c
    return ret

s = "I cannot write in English at all!"

e = chiper(s)
d = chiper(e)

print ("Plain: ")
print (s)

print ("Encoded: ")
print (e)

print ("Decoded: ")
print (d)
