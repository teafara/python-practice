tring):
    rev_string = []
    index = len(first_string) - 1
    while index >= 0:
        rev_string.append(first_string[index])
        index = index - 1
    return ''.join(rev_string)    
   
  
reverse("abc")
reverse ("a")
reverse ("")
