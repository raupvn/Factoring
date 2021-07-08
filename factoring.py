class Factoring:
    def __init__(self):
        self.n1_factors = []
        self.n2_factors = []
        self.display_int_a_factors = []
        self.display_int_b_factors = []

        # wondering whether or not the inclusion of negative factor is even necessary; anyone who is looking for factors
        # of some int is bound to know that signed ints share the same factors as unsigned ints; they would most
        # likely know to change the sign of at least one of the ints factors without me including them in the factor
        # list

    def generate_factors(self, n1, n2):
        """ generates a list of factors by looping through a range of values from 1 to factored int inclusive;
        negative factorization loops through a range that starts at -1 and loops backwards down to the factored int
        inclusive; factors are appended to their respective lists """

        if n1 >= 0:
            for i in range(1, n1 + 1):
                if n1 % i == 0:
                    self.n1_factors.append(i)
        elif n1 <= 0:
            for i in range(-1, n1 - 1, -1):
                if n1 % i == 0:
                    self.n1_factors.append(i)

        if n2 >= 0:
            for j in range(1, n2 + 1):
                if n2 % j == 0:
                    self.n2_factors.append(j)
        elif n2 <= 0:
            for j in range(-1, n2 - 1, -1):
                if n2 % j == 0:
                    self.n2_factors.append(j)

    def find_factor_pairs(self, n1, n2):
        """ factor pairs for individual ints are created by simultaneously looping through two lists containing the
        same factors of the ints argued (one reversed; in descending order); the reversed list, because it contains
        the same factors as its original, only reversed, aligns with the original list in such a way that, when iterated
        through, is paired with the proper multiple needed to produce the argued int """

        self.generate_factors(n1, n2)
        n1_f_rev = sorted(self.n1_factors, reverse=True)
        n2_f_rev = sorted(self.n2_factors, reverse=True)

        print(f"\nThe factor pairs of {n1} are:")

        if n1 >= 0:
            for i in self.n1_factors:
                for j in n1_f_rev:
                    # this condition feels redundant; integers in n(x)_f_rev are factors; they will multiply to the
                    # argued int; could i omit condition entirely?
                    # update: if condition is omitted then the ends of the factor lists get printed as well; this is
                    # a problem because x * x should not = x
                    if i * j == n1:
                        print(f"{i} and {j}")   # try returning a list of factor pairs instead of printing them
        elif n1 <= 0:
            for i in self.n1_factors:
                for j in n1_f_rev:
                    # abs() is used to show at least one unsigned factor of the int (think int arithmetic rules;
                    # different signs yield a negative product)
                    if i * abs(j) == n1:
                        print(f"{i} and {abs(j)}")

        print(f"\nThe factor pairs of {n2} are:")

        if n2 >= 0:
            for k in self.n2_factors:
                for l in n2_f_rev:
                    if k * l == n2:
                        print(f"{k} and {l}")
        elif n2 <= 0:
            for k in self.n2_factors:
                for l in n2_f_rev:
                    if k * abs(l) == n2:
                        print(f"{k} and {abs(l)}")

    def display_factors(self, n1, n2):
        """ similar to generate_factors() except for negative ints loops from the negative int all the way through to
        its positive representation, (skipping 0) """

        # this entire method seems redundant; if i decide to abandon negative factors entirely i could just use the
        # display the n(x)_factors lists

        # note - if argued 0 no factors or factor pairs are displayed

        if n1 >= 0:
            for m in range(1, n1 + 1):
                if n1 % m == 0:
                    self.display_int_a_factors.append(m)
        elif n1 <= 0:
            for m in range(n1, abs(n1) + 1):
                if m == 0:
                    continue
                if n1 % m == 0:
                    self.display_int_a_factors.append(m)

        if n2 >= 0:
            for n in range(1, n2 + 1):
                if n2 % n == 0:
                    self.display_int_b_factors.append(n)
        elif n2 <= 0:
            for n in range(n2, abs(n2) + 1):
                if n == 0:
                    continue
                if n2 % n == 0:
                    self.display_int_b_factors.append(n)

        print(self.display_int_a_factors)
        print(self.display_int_b_factors)
