class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0

        for v in operations:
            if v == '+':
                score += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            
            elif v == 'D':
                score += 2 * stack[-1]
                stack.append(2 * stack[-1])

            elif v == 'C':
                score -= stack.pop()

            else:
                score += int(v)
                stack.append(int(v))
                
        return score





        