###### 2
def print_multiplication_table():
    print("A multiplication table for numbers up to 12:")
    for i in range(14):
        for j in range(14):
            if i == 0 and j == 0:
                print(f"{4 * ' '}", end="")
            elif i == 0:
                print(f"{(j - 1):>4}", end="")
            elif j == 0:
                print(f"{(i - 1):>4}", end="")
            else:
                print(f"{(i - 1) * (j - 1):>4}", end="")
        print()

###### 3
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

###### 4
def combine_lists(input_str1, input_str2):
    combined_list = []

    # Remove brackets and split by commas
    input1 = input_str1.replace("[", "").replace("]", "").split(",")
    input2 = input_str2.replace("[", "").replace("]", "").split(",")

    # if length is not equal, return None
    if len(input1) != len(input2):
        return None

    # Alternately taking elements
    for i in range(len(input1)):
        combined_list.append(input1[i].strip())
        combined_list.append(input2[i].strip())

    return combined_list

###### 5
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        fib1, fib2 = 1, 1
        for _ in range(3, n + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2

###### 6
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



if __name__ == "__main__":
    # Question 2
    print("Question 2")
    print_multiplication_table()

    # Question 3
    print("\nQuestion 3")
    input_str = input("Enter a string (or 'q' to quit): ")
    while input_str.lower() != 'q':
        if is_palindrome(input_str):
            print(f"The string '{input_str}' is a palindrome.")
        else:
            print(f"The string '{input_str}' is not a palindrome.")
        input_str = input("Enter a string (or 'q' to quit): ")
    print("Goodbye!")

    # Question 4
    print("\nQuestion 4")
    input_list1 = input("Enter the first list(format: [a,b,c], [1,2,3]): ")
    input_list2 = input("Enter the second list(format: [a,b,c], [1,2,3]): ")
    combined_list = combine_lists(input_list1, input_list2)
    if combined_list is None:
        print("Error: Lists are not of equal length.")
    else:
        print("Combined list:", combined_list)

    # Question 5
    print("\nQuestion 5")
    for i in range(1, 101):
        print(f"{fibonacci(i)}", end=" ")

    # Question 6
    print("\n\nQuestion 6")
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
