# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append( Bracket(next_character, i + 1))
            # pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack  or  not are_matching(opening_bracket_stack[-1].char, next_character):
               return i + 1
        opening_brackets_stack.pop()
        
 if not opening_brackets_stack:
    return "Success"
else:  
    return opening_brackets_stack[-1].position + 1    
            # pass



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if isinstance(result, int): 
        print (result)
    else:
        print (result)

        

if __name__ == "__main__":
    main()
