class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        second = "*".join([str(len(s)) for s in strs])
        first = "".join(strs)
        return first + "-" + second

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        idx = s.rfind("-")
        first = list(s[:idx])
        second = map(int, s[idx+1:].split("*"))
        
        res = []
        for num in second:
            res.append("".join(first[:num]))
            first[:] = first[num:]
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))