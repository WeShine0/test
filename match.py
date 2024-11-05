def brackets_matched(expression):
    stack = []
    i = 0
    length = len(expression)

    while i < length:
        char = expression[i]

        if char == '/' and i + 1 < length and expression[i + 1] == '/':
            i += 2
            while i < length and expression[i] != '\n':
                i += 1
        elif char == '/' and i + 1 < length and expression[i + 1] == '*':
            i += 2
            while i < length - 1 and not (expression[i] == '*' and expression[i + 1] == '/'):
                i += 1
            i += 2
        elif char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return False
        i += 1
    return len(stack) == 0


def find_matching_bracket(expression, position):
    stack = []
    pairs = {}
    i = 0
    length = len(expression)

    while i < length:
        char = expression[i]

        if char == '/' and i + 1 < length and expression[i + 1] == '/':
            i += 2
            while i < length and expression[i] != '\n':
                i += 1
        elif char == '/' and i + 1 < length and expression[i + 1] == '*':
            i += 2
            while i < length - 1 and not (expression[i] == '*' and expression[i + 1] == '/'):
                i += 1
            i += 2 
        elif char in '([{':
            stack.append((char, i))
        elif char in ')]}':
            if not stack:
                return None
            top, top_pos = stack.pop()
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return None
            pairs[top_pos] = i
            pairs[i] = top_pos
        i += 1
    if position in pairs:
        return pairs[position]
    else:
        return None  
expression=input("Entering the text:")
is_matched = brackets_matched(expression)
if  is_matched:
    print("Brackets are matched.")
    position=int(input("position:"))-1
    matching_position = find_matching_bracket(expression, position)+1  
    if matching_position is not None:
        print(f"The bracket at position {position+1} matches with the bracket at position {matching_position}.")
    else:
        print(f"No matching bracket found for the bracket at position {position}.")
else:
    print("Brackets are not matched.")


