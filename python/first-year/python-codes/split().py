n = int(input())
arr = [0]*n
i=0
arr = [int(i) for i in input().split()]

        

print(arr)
mx=(max(arr))
arr.remove(mx)
mx2=(max(arr))
while mx==mx2:
    arr.remove(max(arr))
    mx2=max(arr)

print(max(arr))

