def info(**details):
    for n, v in details.items():
        print(n.upper().ljust(20), v)


def line(**details):
    ch = '-'
    len = 10
    if 'char' in details:
        ch = details['char']
    if 'len' in details:
        len = details['len']
    for i in range(1, len + 1):
        print(ch, end='')


line(char='*', len=20)
line(len=20)

print()

info(name='Srikanth', mobile="9059057000", langs=['java', 'c#', 'python'])
