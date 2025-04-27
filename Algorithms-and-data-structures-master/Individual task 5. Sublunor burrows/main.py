import sys


input = sys.stdin.readline
n = int(input())
words = [input().strip() for _ in range(n)]


def is_palindrome(s):
    return s == s[::-1]


revDict = {}
for i, w in enumerate(words):
    if w in revDict:
        revDict[w].append(i)
    else:
        revDict[w] = [i]

result = set()
for i, w in enumerate(words):
    L = len(w)
    for j in range(L + 1):
        # Разбиение на A (префикс) и B (суффикс)
        A = w[:j]
        B = w[j:]
        # Если префикс A является палиндромом, ищем подходящие t для B
        if is_palindrome(A):
            candidate = B  # t должно быть = reverse(A) ? Нет, здесь нужно искать t = R(B)
            revB = B[::-1]
            if revB in revDict:
                # Учтите случай, когда найденный индекс равен i (т.е. та же строка)
                # Если требуется учитывать самоконсолидацию, то можно её добавлять
                for k in revDict[revB]:
                    if(i!=k):
                        result.add((i, k))
        # Если суффикс B является палиндромом (j != L, чтобы избежать двойного счета пустого префикса)
        if j != L and is_palindrome(B):
            revA = A[::-1]
            if revA in revDict:
                for k in revDict[revA]:
                    if(i!=k):
                        result.add((k, i))

print(len(result))
