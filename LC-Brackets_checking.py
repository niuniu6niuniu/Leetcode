# Brackets checking

# Example
# "(((())))", "()()()" is True
# "(()))", ")))(((" is False

# Idea: 1. Odd length string -> False
#       2. Recursively remove "()", if sub-str left -> False

def brackets(str):
    if len(str) % 2 == 1:
        return False
    else:
        while str.find('()') != -1:
            str = str.replace('()','')
        if len(str) > 0:
            return False
        else:
            return True

print(brackets("()(())"))
