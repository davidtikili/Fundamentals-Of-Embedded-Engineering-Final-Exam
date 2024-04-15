def verify_add(m, ls):
    seen = set()
    for num in ls:
        diff = m - num
        if diff in seen and diff != num:
            return True
        seen.add(num)
    return False

def main():
    print(verify_add(100, [1, 2, 3, 4, 5]))  
    print(verify_add(7, [1, 2, 3, 4, 2]))     
    print(verify_add(10, [5, 5]))             
    print(verify_add(151, range(0, 200000, 3)))  
    print(verify_add(50004, range(0, 200000, 4))) 
main()
