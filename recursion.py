def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)


def compareTo(s1, s2):
    print(f'Comparing "{s1}" with "{s2}"')

    if not s1 and not s2:
        print("Both strings are empty.")
        return 0
    elif not s1:
        print("s1 is empty.")
        return -1
    elif not s2:
        print("s2 is empty.")
        return 1
    elif s1[0] < s2[0]:
        print(f"{s1[0]} < {s2[0]}")
        return -1
    elif s1[0] > s2[0]:
        print(f"{s1[0]} > {s2[0]}")
        return 1
    else:
        print(f"{s1[0]} == {s2[0]}, continue with the rest of the strings")
        return compareTo(s1[1:], s2[1:])


if __name__ == '__main__':
    answer = fibonacci(33)
    print(answer)

    thegcd = gcd(396198,713394)
    print(thegcd)

    print("---------------------------------")
    print("Result:", compareTo("two", "two"))  # should return 0
    print("---------------------------------")
    print("Result:", compareTo("two", "twi"))  # should return 1
    print("---------------------------------")
    print("Result:", compareTo("twe", "two"))  # should return -1
