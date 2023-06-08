# Data types and string manipulation

# Strings
s = "Hello, world!"
print(s[0], end="")
print(s[4], end="")
print(s[2], end="")
print(s[2], end="")
print(s[4], end="")
print(s[7], end="")
print(" world!")

# Integers
print(123_456_789)
print(8 * 8)

# Floats
print(3.141)

# Booleans
True
False


# Type Error, Type checking and type conversion (str, int, float)
length = len(input("What is your name? "))
print(type(length))

length_str = str(length)

print("Your name has " + length_str + " characters")


# Math Operations

# PEMDAS(L-R) (Oder of priority for mathematical operations)

2 + 2  # additon
5 - 3  # subtraction
6 / 2  # division
4 * 7  # multiplication
4 ** 3 # power
6 % 4  # modulo (remainder of)


# f'Stings and Number manipulation
# round() function
print(round(8/3))
# round to two decimal places
print(round(8/3, 2))
#floor division
print(8 // 3)

# f'Strings usage
print(f"Using f'Strings now, you name {length} characters")
