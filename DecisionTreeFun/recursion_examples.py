# this code is adapted to python from my C++ recursion examples here: https://github.com/GonzagaCPSC122/RecursionFun/tree/master
# see the corresponding recursion videos in this playlist: https://youtube.com/playlist?list=PL7uPCUbavAWcpim5348ad79x6yZ1N73Gf&si=zhVyHI3LucAlSiVm
# see the recursion assignment here for practice problems: https://docs.google.com/document/d/1yN_JXoIyfhlDAka9UzIMyury2LXQgopEQOH9f9jpVHw/edit?tab=t.0#heading=h.6diexf3ifwty

# a recursive function: a function that directly (or indirectly) calls itself
# pro: simple/short/elegant solutions for some problems (compared to iterative solutions)
# commonly used by other programmers
# con: high memory overhead (compared to iterative solutions)
def iterative_countdown(n):
    for i in range(n, 0, -1):
        print(i, end=" ")
    print("blastoff!!")

def recursive_countdown(n):
    if n == 0:
        print("blastoff!!")
        return
    print(n, end=" ")
    recursive_countdown(n - 1)
    print(f"returning from the {n - 1} call")

def iterative_multiplication(m, n):
    result = 0
    for _ in range(n):
        result += m
    return result

def recursive_multiplication(m, n):
    if n == 1:
        return m
    return m + recursive_multiplication(m, n - 1)

def iterative_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def recursive_power(base, exponent):
    if exponent == 1:
        return base
    return base * recursive_power(base, exponent - 1)

def iterative_factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)

def display_string(s, index=0):
    if index == len(s):
        print()
        return
    print(s[index], end="")
    display_string(s, index + 1)

def display_string_alt(s):
    if not s:
        print()
        return
    print(s[0], end="")
    display_string_alt(s[1:])

def display_string_reverse(s):
    if not s:
        return
    display_string_reverse(s[1:])
    print(s[0], end="")

def count_characters(s):
    if not s:
        return 0
    return 1 + count_characters(s[1:])

def fun(n):
    if n > 2:
        fun(n - 1)
        fun(n - 2)
        fun(n - 3)
    print(n)

def more_fun(n):
    print(n)
    if n > 2:
        more_fun(n - 1)
        more_fun(n - 2)
        more_fun(n - 3)

print("iterative countdown")
iterative_countdown(3)
print()
iterative_countdown(10)
print()

print("recursive countdown")
recursive_countdown(3)
print()
recursive_countdown(10)
print()

print("iterative multiplication")
print(iterative_multiplication(2, 3))
print("recursive multiplication")
print(recursive_multiplication(2, 3))
print()

print("iterative power")
print(iterative_power(2, 3))
print("recursive power")
print(recursive_power(2, 3))
print()

print("iterative factorial")
print(iterative_factorial(3))
print()
print(iterative_factorial(5))
print("recursive factorial")
print(recursive_factorial(3))
print()
print(recursive_factorial(5))
print()

print("display string")
display_string("hello")
display_string("recursion")
print("display string alt")
display_string_alt("hello")
display_string_alt("recursion")
print()

print("display string reverse")
display_string_reverse("hello")
print()
display_string_reverse("recursion")
print()

print("count characters")
print(count_characters("hello"))
print(count_characters("recursion"))
print()

print("fun")
fun(5)
print()
more_fun(5)
print()