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
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack  or  not are_matching(opening_bracket_stack[-1].char, next):
               return i + 1
        opening_brackets_stack.pop()
        
        if not opening_brackets_stack:
            return "Success"
        else:
            return opening_brackets_stack[-1].position + 1    
            pass



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if isinstance(mismatch, int): 
        print (mismatch)
    else:
        print (mismatch)

in = input()
if in == 'I':
    result = mismatch(text)
    print(result)
else:
    with open ("test_file.txt", "r") as file:
        for line in file:
            write = line.strip()
            result = mismatch(text)
            print(result)
        

if __name__ == "__main__":
    main()
