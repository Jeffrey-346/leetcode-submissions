class Solution:

    def encode(self, strs: List[str]) -> str:
        # begin with the size of the string
        # add delimiter
        # add string
        #repeat
        encoded_str = ""
        for s in strs:
            size = len(s)
            encoded_str += str(size) + "|" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # determine size of string by splitting on delimiter
        # process each char and reconcatinate into original str
        # repeat until s is empty
        decoded_list = []
        next_str = s
        while next_str:
            #split by delimiter and get size
            tokens = next_str.split("|", maxsplit=1)
            size = int(tokens[0])
            # use size to get str and add it to list
            curr_str = tokens[1][0:size]
            decoded_list.append(curr_str)
            # get next string
            next_str = tokens[1][size:]
        return decoded_list



