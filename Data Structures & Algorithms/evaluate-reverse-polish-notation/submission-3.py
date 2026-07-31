class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        for token in tokens:
            
            if token == "+":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(a+b)
            elif token == "/":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(int(b/a))
            
            elif token == "*":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(a*b)

            elif token == "-":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b-a)
            else:
                stack.append(int(token))
        return stack[0]

            