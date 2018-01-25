s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s.replace(".","")
s.replace(",","")
print ([(word, len(word)) for word in s.split()] )
