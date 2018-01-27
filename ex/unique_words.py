
st = "How is this. This is fine"

words = set()
for w in st.split(' '):
    words.add(w.strip(".,").upper())

for w in sorted(words):
    print(w)

print(words)

