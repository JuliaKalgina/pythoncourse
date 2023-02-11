your_word = input('')


def rev_str(a):
    emptystr = ""
    for i in range(len(a)-1, -1, -1):
        emptystr = emptystr + a[i]
    return emptystr


new_str = rev_str(your_word)
if new_str == your_word:
    print('It is a palindrome!')
else:
    print('It is not a palindrome.')