''' 
    Calculate phenotypic breakdown of a population 
    given amount of homozygous recessive offspring

    Hardy Weinberg Equations:
    p + q = 1
    p^2 + 2pq + q^2 = 1

    Prompts the user for data via the terminal.
'''

from math import sqrt

# get data from user
print()
homo_rec = float(input("number of homozygous recessive individuals:  "))
total = float(input("total number of individuals:  "))

# calculate
q2 = homo_rec/total
q = sqrt(q2)
p = 1 - q
p2 = p**2
_2pq = 2 * p * q

# print info back to user
print()
print("p = ", p)
print("q = ", q)
print()
print("p^2 = ", round(p2, 3))
print("2pq = ", round(_2pq, 3))
print("q^2 = ", round(q2, 3))
print()
print("num AA = ", round(p2*total,2))
print("num Aa = ", round(_2pq*total,2))
print("num aa = ", homo_rec)

