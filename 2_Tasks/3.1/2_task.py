def finder(s, k):
    count = 0
    while s.find(k) != -1:
        count += 1
        s = s[s.find(k)+1:]
    return count


s = input()
k = input()

print(finder(s, k))

