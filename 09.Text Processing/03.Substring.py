def substring(rmv, txt: str):
    while rmv in txt:
        txt = txt.replace(remove_this, "")
    return txt


remove_this = input()
data = input()
print(substring(remove_this, data))
