def finding_the_palindromes(num):
    for ele in num:
        rev = ele[::-1]
        if ele == rev:
            print("True")
        else:
            print("False")


nums = input().split(", ")

finding_the_palindromes(nums)