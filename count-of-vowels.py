#count of vowels
def count_vowel(s):
    vowel=('a','e','i','o','u')
    count=0
    for char in s:
        if char in vowel:
            count+=1
    return count
print(count_vowel("Hello World!"))
print(count_vowel("Python Programming"))
    
