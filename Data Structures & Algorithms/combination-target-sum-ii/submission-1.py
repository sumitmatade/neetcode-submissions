class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no need to continue
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])

                backtrack(i + 1, path, total + candidates[i])

                path.pop()

        backtrack(0, [], 0)

        return res