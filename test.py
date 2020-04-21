a = input()
e = len(a)
for i in range(e//2):
    if a[i] != a[-1-i]:
        print("не полиндром")
        quit()
print("полиндром")