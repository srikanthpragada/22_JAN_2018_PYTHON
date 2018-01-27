
st = "How is this. This is fine"
word = "is"
newst = ""
for w in st.split(' '):
    w = w.strip('.')
    print(w)
    if  w == word:
        newst += " * "
    else:
        newst += w + " "


print(newst)



