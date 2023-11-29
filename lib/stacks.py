def is_balanced(expression):
    bracket_stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}

    for char in expression:
        if char in brackets.keys():  
            bracket_stack.append(char)
        elif char in brackets.values():   
            if not bracket_stack or brackets[bracket_stack.pop()] != char:
                return False

   
    return not bracket_stack


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2)) 

