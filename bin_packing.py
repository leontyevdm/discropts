def bin_packing (size, min_index, packing, items, bins, counter):
    global min
    for i in range(min_index, len(items)):
        for j in range(0,len(bins)):
            if bins[j] + items[i][0] <= size:
                if counter <= min:
                    items[i][1] = j
                    bins[j] += items[i][0]
                    if (bins[j] == items[i][0]):
                        counter += 1
                    bin_packing(size, i+1, packing, items, bins, counter)
                    items[i][1] = -1
                    bins[j] -= items[i][0]
                else:
                    return
    if items[len(items) - 1][1] == -1:
        return
    if counter < min:
        min = counter
        for i in range(len(items)):
            packing[items[i][2]] = items[i][1]
    return

n = int(input())
size = int(input())
items = []
packing = [0] * n
bins = [0] * n
for i in range(n):
    items.append([int(input()), -1, i])
sorted_items = sorted(items, key=lambda item: -item[0])
min = n
bin_packing(size, 0, packing, sorted_items, bins,0)
for i in packing:
    print(i+1, end=' ')
