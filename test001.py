import itertools

count = 0
sourceArray = [1, 2, 3, 4]
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            if (sourceArray[i] != sourceArray[j]) \
                    and (sourceArray[j] != sourceArray[k]) \
                    and (sourceArray[i] != sourceArray[k]):
                print(sourceArray[i], sourceArray[j], sourceArray[k])
                count += 1

print(count)

count = 0

for i in itertools.permutations(sourceArray, 3):
    print(i)
    count += 1
print(count)

