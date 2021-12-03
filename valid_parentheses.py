def isValid(s: str) -> bool:
    kv_pairs = {"(":")", "[":"]", "{":"}"}
    if len(s) % 2 != 0 or len(s) < 1 or len(s) > 104 or (s[0] in kv_pairs.values()):
        return False
    lst  = []
    for i in range(len(s)):
        if s[i] in kv_pairs.keys():
            lst.append(s[i])
        elif s[i] in kv_pairs.values() and s[i] == kv_pairs[s[i - 1]]:
            lst.append(s[i])
            if len(lst) == 2:
                lst = []
            else:
                lst = lst[:i-1]
        else:
            return False

        if not lst:
            return True
        else:
            return False
    
if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("Valid")
    else:
        print("False")
