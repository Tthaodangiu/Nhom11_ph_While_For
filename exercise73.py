phrase = input('Enter a phrase: ')
def preprocess_string(s):
    return ''.join(char.lower() for char in s if char.isalnum())
preprocessed_phrase = preprocess_string(phrase)
n = len(preprocessed_phrase)
m = n // 2
print('The phrase "', phrase, '" is ', sep='', end='')
for i in range(m):
    if preprocessed_phrase[i] != preprocessed_phrase[-1 - i]:
        print('not ', end='')
        break
print('a palindrome')
