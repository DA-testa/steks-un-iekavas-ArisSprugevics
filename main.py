# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next) #Bracket(next,i+1)
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            if not bool(opening_brackets_stack) or not are_matching(opening_brackets_stack.pop(),next):
                return(i+1)
            # Process closing bracket, write your code here
            # opening_brackets_stack.pop()
            pass




def main():
    text = input()
    if text == "I":
        text = input()
        mismatch = find_mismatch(text)

        if mismatch is None:
            print("Success")
        else:
            print(mismatch)

    elif text == "F":
        j = 0
        while j < 6:
            with open('test/'+str(j)) as f:
                text = f.readline()
            mismatch = find_mismatch(text)

            if mismatch is None:
                print("Success")
            else:
                print(mismatch)
            j = j+1
    else:
        print("unknown command")
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
