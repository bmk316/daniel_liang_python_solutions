# COUNT digit occurrences in string
def count_digits(inp):
    # for a,b in sorted((c, inp.count(c)) for c in set(inp)):
    for a, b in sorted((c, inp.count(c)) for c in set(inp) if c.isdigit()):
        print("{} occurs {} times".format(a, b))


my_string = input("Enter string of numbers: ")
count_digits(my_string)

