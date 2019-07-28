def removeDuplicates(S):
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            S = S.replace(S[i] * 2, '')
            break
    else:
        return S
    S = removeDuplicates(S)
    return S


print(removeDuplicates('123322'))
