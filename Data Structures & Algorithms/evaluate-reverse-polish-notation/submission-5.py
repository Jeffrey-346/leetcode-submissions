class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # pretty much we have the first operand as the prev res, move 
        # forward for the second operand, and then move forward for the    
        # operation
        stack = []
        ptr = 0
        while ptr < len(tokens):
            if tokens[ptr] not in {"+", "-", "*", "/"}:
                stack.append(int(tokens[ptr]))
            elif tokens[ptr] == "+":
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(first_operand + second_operand)
            elif tokens[ptr] == "-":
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(first_operand - second_operand)
            elif tokens[ptr] == "*":
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(first_operand * second_operand)
            elif tokens[ptr] == "/":
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(int(first_operand / second_operand))
            ptr += 1
        return stack[0]





        