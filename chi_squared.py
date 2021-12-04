''' 
    Calculate the Chi-Squared value to determine whether or not 
    a significant difference exists 
    between an observed data set and the expected results

    Prompts the user for data via terminal.
'''


from sys import exit

expected = []
observed = []

x2 = 0.0

possible_outcomes = int(input("number of possible outcomes:  "))

# get data from user about corresponding expected and observed values
for i in range(possible_outcomes):
    n = "expected value " + str(i+1) + ":  "
    m = "observed value " + str(i+1) + ":  "

    e = input(n)
    o = input(m)

    expected.append(e)
    observed.append(o)


string = "chi squared = "

#calculate chi squared
for n in range(len(observed)):
    o = float(observed[n])
    e = float(expected[n])

    x = ((o-e)**2)/e
    x2 += x

    x = round(x, 4)
    if n == 0:
        string += str(x)
    else:
        string += " + "
        string += str(x)

round(x2, 5)

print()
print("work:  " + string)
print("chi squared = ", x2)


deg_free = possible_outcomes - 1
critical = 0
table = [0.0, 3.84, 5.99, 7.82, 9.49, 11.07, 12.59, 14.07, 15.51]

if deg_free > len(table):
    print("degrees of freedom greater than what is in this stored in this program")
    exit(1)
else:
    critical = table[deg_free]


print()
print("degrees of freedom: ", deg_free)
print("critical value: ", critical)
print()

# determine whether the null hypothesis is accepted or rejected by comparing chi squared to critcal value
if x2 < critical:
    print(x2, "<", critical)
    print("null hypothesis: accepted")
    print("no significant difference")
elif x2 > critical:
    print(x2, ">", critical)
    print("null hypothesis: rejected")
    print("significant difference")