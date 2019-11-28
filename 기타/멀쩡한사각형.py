def solution(w,h):
    answer = w*h
    cut = 0
    prev = 0
    width = w
    height = h
    while(h):
        t = w % h
        w = h
        h = t
        
    cut = (width//w + height//w -1)  # ???
    answer -= cut * w
    return answer


#############################################
def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)   # ???