
st = "Python is a wonderful language. It is used for all purposes!"

words = []
for w in  st.split(" "):
    if len(w) > 5:
        words.append(w.strip(".!").upper())

for w in  sorted(words):
    print(w)


