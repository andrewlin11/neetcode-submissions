class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstring = ''
        for s in strs:
            encodedstring += (";l;" + s)
        return encodedstring

    def decode(self, s: str) -> List[str]:
        decodedlist = s.split(";l;")
        return decodedlist[1:]