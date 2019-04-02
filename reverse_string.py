def reverse(first_string):
    rev_string = []
    index = len(first_string) - 1
    while index >= 0:
        rev_string.append(first_string[index])
        index = index - 1
    return ''.join(rev_string)    
   
  
print(reverse("abc"))
print(reverse("a"))
print(reverse(""))
print(reverse("goonies"))
