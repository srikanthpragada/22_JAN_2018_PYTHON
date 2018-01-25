# Display all positions where a substring is present in main string

st = "How are you? Hope you are fine!"
sub = "o"
start  = 0

while True:
    pos = st.find(sub,start)
    if pos == -1:
        break

    print(pos)
    start = pos + 1




