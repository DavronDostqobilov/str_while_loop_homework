def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=len(s)
    while i<len(s):
        if s[i].isalnum():
            n=n-1
        i+=1
    return n
print(main('#davro%^n@'))