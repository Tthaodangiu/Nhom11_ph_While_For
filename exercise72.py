#Tìm từ đối xứng
word = input('Enter a word: ')

n = len(word)
m = n//2
print('The word "', word, '" is ', sep='', end='')
for i in range(m):
    if word[i] != word[-1-i]:
        print('not ', end='')
        break
print('a palindrome')