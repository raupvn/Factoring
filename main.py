from factoring import Factoring


factors = Factoring()

while True:
    print("\nEnter two integers to see their factors:"
          "\n(enter 'q' to quit)"
          "\n")
    n1 = input("Integer 1: ")
    if n1 == 'q':
        break
    n2 = input("Integer 2: ")
    if n2 == 'q':
        break
    factors.display_factors(int(n1), int(n2))
    factors.find_factor_pairs(int(n1), int(n2))
