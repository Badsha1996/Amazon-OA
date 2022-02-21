class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_stack = []
        let_stack = []
        for log in logs:
            t = log.split()
            idnt, vals = t[0], ' '.join(t[1:])
            if vals[0].isdigit():
                dig_stack.append(log)
            else:
                let_stack.append((idnt, vals))
        let_stack.sort(key=lambda x: (x[1],x[0]))
        return [f'{x} {y}' for x,y in let_stack] + dig_stack