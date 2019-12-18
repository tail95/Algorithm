import sys
T = int(sys.stdin.readline().rstrip())
while T:
    aa, bb = sys.stdin.readline().rstrip().split()
    a, b = map(list,(aa,bb))
    if len(a)!=len(b):
        print(aa + " & " + bb + " are NOT anagrams.")
        T-=1
        continue
    for fr in a:
        if fr in b:
            b.pop(b.index(fr))
        else:
            print(aa + " & " + bb + " are NOT anagrams.")
            break
    if not b:
        print(aa + " & " + bb + " are anagrams.")
    T-=1