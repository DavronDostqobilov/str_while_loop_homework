def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=0
    while i<len(s):
        if s[i].isalpha():
            n+=1
        i+=1
    return n
print(main('8787asdc8'))