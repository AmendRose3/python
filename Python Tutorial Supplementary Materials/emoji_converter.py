msg=input(">")
words=msg.split(' ')
print(words)
map={
    ":)":"😊",
    ":(":"😒",
    ";)":"😉"
}

out=" "
for word in words:
    out+=map.get(word,word) + " "

print(out)