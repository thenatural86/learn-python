# Write your code here


def my_func(filename):
    d = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(":")[0]
            flower = line.split(": ")[1].strip()
            d[letter] = flower
        return d


def main():
    name = input("Enter your First [space] Last name only:")
    flower = my_func("flowers.txt")
    first_name = name[0]
    first_letter = name[0]

    print("Unique flower name with the first letter: {}".format(
        flower[first_letter]))


#     print(flower)
main()

# HINT: create a dictionary from flowers.txt

# HINT: create a function to ask for user's first and last name


# print the desired output
