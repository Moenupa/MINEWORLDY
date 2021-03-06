'''
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
mid = [2.5, 7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 62.5, 67.5, 72.5, 77.5]

rate = [0.7045454545454546, 0.35, 0.5789473684210527, 0.34375, 0.3442622950819672, 0.3298245614035088, 0.4659090909090909, 0.417910447761194, 0.3617021276595745, 0.41025641025641024, 0.4166666666666667, 0.3888888888888889, 0.2857142857142857, 0.0, 0.0, 1.0]

female_rate = [0.7619047619047619, 0.3, 0.75, 0.7352941176470589, 0.7555555555555555, 0.7078651685393258, 0.8666666666666667, 0.8, 0.6111111111111112, 0.7692307692307693, 1.0, 0.8333333333333334, 1.0, 0, 0, 0]

male_rate = [0.6521739130434783, 0.4, 0.2857142857142857, 0.12903225806451613, 0.1038961038961039, 0.15816326530612246, 0.25862068965517243, 0.19047619047619047, 0.20689655172413793, 0.23076923076923078, 0.125, 0.16666666666666666, 0.09090909090909091, 0.0, 0.0, 1.0]

plt.bar(x=mid, height=rate, width=5)

plt.plot(mid[:-3], female_rate[:-3], 'r', label="Female Survival Rate")

plt.plot(mid, male_rate, 'y', label="Male Survival Rate")
plt.show()
'''
def isPrime(n): 
    if n <= 1: 
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True


if __name__ == "__main__":
    upbound = int(input("input message"))
    string = ""
    count = 0

    for i in range(upbound, 0, -1):
        if not isPrime(i):
            string = count * " " + str(i) + "\n" + string
            count += 1
            
    print(string[:-1])