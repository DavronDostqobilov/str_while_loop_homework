def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    sum=0
    while i<len(s):
        if s[i].isdigit():
            sum=sum+int(s[i])
        i+=1
    return sum
print(main('wd1342'))