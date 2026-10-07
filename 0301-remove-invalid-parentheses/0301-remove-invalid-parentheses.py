class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        min_ = n
        result = []

        def backtrack(index, cnt, mask, balance):
            nonlocal min_, result

            # Finished
            if index == n:
                if balance != 0:
                    return

                if cnt < min_:
                    min_ = cnt
                    result = [mask]
                elif cnt == min_:
                    result.append(mask)

                return
            
            if cnt > min_:
                return
                
            if s[index].isalpha():
                new_mask = mask | (1 << index)
                backtrack(index+1, cnt, new_mask, balance)
                return
            # ----------------
            # KEEP s[index]
            # ----------------
            if s[index] == "(":
                new_balance = balance + 1
            else:
                new_balance = balance - 1

            if new_balance >= 0:
                # Set bit index -> keep
                new_mask = mask | (1 << index)

                backtrack(
                    index + 1,
                    cnt,
                    new_mask,
                    new_balance
                )

            # ----------------
            # REMOVE s[index]
            # ----------------
            backtrack(
                index + 1,
                cnt + 1,
                mask,
                balance
            )

        backtrack(0, 0, 0, 0)

        # Convert masks to strings
        answers = []

        for mask in result:
            curr = []

            for i in range(n):
                if mask & (1 << i):
                    curr.append(s[i])

            answers.append("".join(curr))

        return list(set(answers))