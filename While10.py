def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    sum=0
    while i<len(s):
        if s[i].isdigit():
            if int(s[i])%2==1:
                sum=sum+int(s[i])
        i+=1
    return sum
print(main('wd1342'))