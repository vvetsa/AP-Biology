''' 
    For the problems that combine using the Hardy-Weinberg Equations and a Chi-Squared Analysis.
    
    Used to determine whether a population is in Hardy-Weinberg Equilibrium
    or if allele frequencies are changing and the population is evolving

    Prompts the user for data via the terminal.
'''

from math import sqrt

class Population():
    
    def __init__(self, name, aa = 0.0, total = 1.0):
        self.name = name
        
        self.total = total      # total number of individuals in population
        
        self.p = 0.0            # p = freq of dominant allele in population
        self.q = 0.0            # q = freq of recessive allele in population

        self.p2 = 0.0
        self.pq2 = 0.0
        self.q2 = aa

        self.AA = 0.0           # AA = number of homozygous dominant individuals
        self.Aa = 0.0           # Aa = number of heterozygous individuals
        self.aa = aa            # aa = number of homozygous recessive individuals

    def get_data(self):
        '''
        get data from the user
        calculate the relevant variables from the given information
        '''

        print() # blank line for readability

        # get data from user
        aa = float(input(f"number of {self.name} homozygous recessive individuals:  "))
        total = float(input(f"total number of {self.name} individuals:  "))

        self.aa = aa
        self.total = total

        # calculate information from user data  
        q2 = aa/total       # q2 = q^2
        q = sqrt(q2)
        p = 1 - q
        p2 = p**2           # p2 = p^2
        pq2 = 2 * p * q     # pq2 = 2pq = 2 * p * q NOT p * q^2

        self.q2 = round(q2, 3)
        self.q = round(q, 3)
        self.p = round(p, 3)
        self.p2 = round(p2, 3)
        self.pq2 = round(pq2, 3)

        Aa = pq2 * total
        AA = p2 *  total

        self.Aa = round(Aa, 3)
        self.AA = round(AA, 3)

    def print_data(self):
        '''
        print the data in an easily readable format such that work can be written 
        '''
        print()
        print(self.name, ": ")
        print()
        print("p = ", self.p)
        print("q = ", self.q)
        print()
        print("p^2 = ", round(self.p2, 3))
        print("2pq = ", round(self.pq2, 3))
        print("q^2 = ", round(self.q2, 3))
        print()
        
        '''
        print("num AA = ", self.AA)
        print("num Aa = ", self.Aa)
        print("num aa = ", self.aa)
        '''

def calc_X2(E, O):
    '''
    Calculate the Chi-Squared value to determine whether or not the null hypothesis is rejected
        null hypothesis: the population IS in hardy-weinberg equilibrium

        E = Expected Population
        O = Observed Population
    '''


    ''' remember scale to total of observed '''
    E_AA = float(E.p2 * O.total)
    E_Aa = float(E.pq2 * O.total)
    E_aa = float(E.q2 * O.total)

    print()
    print(f"scaled expected values:\tAA: {E_AA}\tAa: {E_Aa}\taa: {E_aa}")
    print(f"observed values:\tAA: {O.AA}\tAa: {O.Aa}\taa: {O.aa}")

    expected = [E_AA, E_Aa, E_aa]
    observed = [O.AA, O.Aa, O.aa]

    # actually calculating chi-squared with the work
    string = "chi squared = "
    x2 = 0
    for n in range(3):
        o = float(observed[n])
        e = float(expected[n])

        x = ((o-e)**2)/e
        x2 += x

        x = round(x, 2)
        if n == 0:
            string += str(x)
        else:
            string += " + "
            string += str(x)

    critical = 5.991

    print()
    print("work:  " + string)
    print("chi squared = ", x2)
    print("\ndeg of freedom: 2 \ncritical value: 5.991\n")
    if x2 < critical:
        print(x2, "<", critical)
        print("null hypothesis: accepted")
        print("Hardy-Weinberg equilibrium")
    elif x2 > critical:
        print(x2, ">", critical)
        print("null hypothesis: rejected")
        print("not in Hardy-Weinberg equilibrium")



expected = Population("expected")
observed = Population("observed")

expected.get_data()
observed.get_data()

expected.print_data()
observed.print_data()

calc_X2(expected, observed)