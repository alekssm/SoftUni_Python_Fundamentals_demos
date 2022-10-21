words = input().split()
word = input()

pals = [ele for ele in words if ele == ele[::-1]]

print(pals)
print(f"Found palindrome {words.count(word)} times")