star = 9
i = 1 if star % 2 == 1 else 2

for i in range(i, star+1, 2):
    print('{0}{1}{0}'.format(' '*((star-i)//2), '*'*i))
for i in range(i-2, 0, -2):
    print('{0}{1}{0}'.format(' '*((star-i)//2), '*'*i))