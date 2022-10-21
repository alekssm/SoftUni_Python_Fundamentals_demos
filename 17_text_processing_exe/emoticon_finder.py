text = input()

while ":" in text:
    ind = text.index(":")
    if not text[ind+1].isspace():
        emoticon = text[ind] + text[ind+1]
        print(emoticon)
    text = text.replace(":", "1", 1)
