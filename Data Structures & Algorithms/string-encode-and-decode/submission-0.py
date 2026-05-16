class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded
    def decode(self, s: str) -> List[str]:
        strs = []

        # Find delimiter
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract length
            x = int(s[i:j])
            # Shift ahead of delimiter
            i = j+1
            strs.append(s[i:i+x])
            i += x

        return strs