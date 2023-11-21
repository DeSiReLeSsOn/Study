import random
def quick_sort(c):
    if len(c) > 1:
        x = c[random.randint(0, len(c)-1)]
        low = [u for u in c if u < x]
        center = [u for u in c if u == x]
        high = [u for u in c if u > x]
        c = quick_sort(low) + center + quick_sort(high)

    return c

print(quick_sort([1,5,7,-3,-9,11]))