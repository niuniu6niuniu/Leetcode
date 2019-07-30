# Brackets checking

# Example
# "(((())))", "()()()" is True
# "(()))", ")))(((" is False

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
