class Solution:
    def valid(self, s, start, length):
        return length == 1 or (s[start] != '0' and (length < 3 or s[start:start+length] <= "255"))

    def restoreIpAddresses(self, s):
        stack = [(0, [], 0)]  # (start, path, segment_count)
        ans = []

        while stack:
            start, path, segment_count = stack.pop()

            if start == len(s) and segment_count == 4:
                ans.append(".".join(path))
                continue

            for length in range(1, 4):
                if start + length > len(s):
                    break

                if self.valid(s, start, length):
                    stack.append((start + length, path + [s[start:start+length]], segment_count + 1))

        return ans