def isIsomorphic(self, s: str, t: str) -> bool:
    
    char_map = {}
    mapped = set()
    for i, char_s in enumerate(s):
        char_t = t[i]
        if char_s in char_map:
            if (char_map[char_s] != char_t):
                return False
        else:
            if char_t in mapped:
                return False
            else:     
                char_map[char_s]= char_t
                mapped.add(char_t)


    return True
