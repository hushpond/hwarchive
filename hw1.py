def archivehw1(x):

    # 약수들의 리스트입니다. 1은 언제나 모든 자연수의 약수입니다.
    divisors = [1]
    # 제곱근을 활용해서 약수를 찾는 과정입니다.
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            divisors.append(i)
            # 자기 자신을 약수 리스트에 추가하지 않도록 합니다.
            if x // i != i:
                divisors.append(x // i)

    closest_sum = sum(divisors)
    closest_combination = divisors

    # 약수들의 합이 x와 같다면, 그 조합을 그대로 리턴합니다.
    if closest_sum == x:
        return closest_combination

    # 모든 약수들의 조합의 경우의 수를 순환합니다.
    num_divisors = len(divisors)
    for i in range(1 << num_divisors):
        combination = [divisors[j] for j in range(num_divisors) if i & (1 << j)]
        total = sum(combination)
        #가장 근사한 합을 찾아냅니다.
        if abs(total - x) < abs(closest_sum - x):
            closest_sum = total
            closest_combination = combination

    return closest_combination

from lab2_p6 import archivehw1
from time import time

testcases = [5, 32, 100, 550, 1096, 1300, 1539, 1804, 1995]

for x in testcases:
    start_t = time()
    lod = archivehw1(x)
    elapsed_time = time() - start_t
    lod.sort()
    flag = True
    for d in lod:
        if x % d > 0:
            flag = False
            break
    print(f"Input:{x: 5d}, Elapsed time: {elapsed_time:.5f}, List: {lod}, Sum: {sum(lod)}, {'All divisors are valid' if flag else 'Some invalid divisor exists'}")

