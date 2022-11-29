def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    n=0
    while i<len(s):
        if  s[i].lower()=='a' or s[i].lower()=='e' or s[i].lower()=='i' or s[i].lower()=='o' or s[i].lower()=='u':
            n+=1
        i+=1
    return len(s)-n
    
print(main('BREAND'))