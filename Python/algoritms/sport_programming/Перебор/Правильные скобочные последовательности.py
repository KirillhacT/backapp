stack = []

def get_correct_sequence(string: str) -> bool:
    for i in string:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            cur = stack.pop()
            if (cur == "(" and i != ")"):
                return False
    return len(stack) == 0

print(get_correct_sequence("(())"))
