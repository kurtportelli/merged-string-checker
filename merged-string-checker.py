# The old_same was added as an attempt to handle banana strings with repeated characters.
# This attempt was not successful for all cases and I thus concluded that this problem
# could not be solved without recursion, which offers a much more elegant solution too.
def is_merge(s, p1, p2):
    si, p1i, p2i = 0, 0, 0
    same, switched = False, False
    old_same = None
    while si < len(s):
        char = s[si]
        if switched == False:
            if p1[p1i:]:
                if p2[p2i:]:
                    if old_same != p1[p1i] == p2[p2i]:
                        same = True
                        switched = False
                        si_same = si
                        p1i_same = p1i
                        p2i_same = p2i
                        old_same = p1[p1i]
        else:
            switched = False
        if p1[p1i:]:
            if char == p1[p1i]:
                si += 1
                p1i += 1
                continue
        if p2[p2i:]:
            if char == p2[p2i]:
                si += 1
                p2i += 1
                continue
        if same == True and switched == False:
            si = si_same
            p1, p2 = p2, p1
            p1i, p2i, = p2i_same, p1i_same
            same, switched = False, True       
            old_same = None
            continue
        return False
    if not p1[p1i:] and not p2[p2i:]:
        return True
    else:
        return False
