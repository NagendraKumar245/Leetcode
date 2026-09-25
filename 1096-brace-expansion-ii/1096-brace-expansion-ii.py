class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        
        stack = []
        cur_union = []
        cur_prod = [{""}]
        
        for ch in expression:
            if ch.isalpha():
                cur_prod = [{p + ch} for p in cur_prod[0]]
                merged = set()
                for s in cur_prod:
                    merged.update(s)
                cur_prod = [merged]
                
            elif ch == '{':
                stack.append((cur_union, cur_prod))
                cur_union = []
                cur_prod = [{""}]
                
            elif ch == ',':
                cur_union.append(cur_prod[0])
                cur_prod = [{""}]
                
            elif ch == '}':
                cur_union.append(cur_prod[0])
                group_res = set().union(*cur_union)
                
                prev_union, prev_prod = stack.pop()
                
                cur_prod = [{a + b for a in prev_prod[0] for b in group_res}]
                cur_union = prev_union
                
        cur_union.append(cur_prod[0])
        final_set = set().union(*cur_union)
        
        return sorted(list(final_set))