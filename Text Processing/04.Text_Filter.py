def text_filter(ban, txt: str):
    for i in range(len(ban)):
        while ban[i] in txt:
            txt = txt.replace(banned_words[i], "*" * len(banned_words[i]))
    return txt


banned_words = input().split(", ")
given_text = input()
print(text_filter(banned_words, given_text))
