class ParenthesesValidator:
    def __init__(self, s):
        self.s = s
    
    def is_valid(self):
        stack = []
        opening_brackets = "({["
        closing_brackets = ")}]"
        brackets_map = {")": "(", "}": "{", "]": "["}
        
        for char in self.s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or stack.pop() != brackets_map[char]:
                    return False
        
        return not stack


# Example usage
input_string = "({[{()}]})"
validator = ParenthesesValidator(input_string)
print(validator.is_valid())  # Output: True
