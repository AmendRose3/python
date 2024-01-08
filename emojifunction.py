
def emoji(msg): 
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
    return out



msg=input(">")
out=emoji(msg)
print(out)