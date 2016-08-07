"""
In mathematics, Stirling's approximation (or Stirling's formula) is an
approximation for factorials. It is a very powerful approximation, leading to
accurate results even for small values of n. It is named after James
Stirling, though it was first stated by Abraham de Moivre.

n!\sim {\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}.
"""

import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(
    description="In mathematics, Stirling's approximation (or Stirling's "
                "formula) is an approximation for factorials. It is a very "
                "powerful approximation, leading to accurate results even for "
                "small values of n. It is named after James Stirling, though "
                "it was first stated by Abraham de Moivre.")
parser.add_argument("-n", type=int,
                    help="The n factorial.")
args = parser.parse_args()

# Load the memo (dynamic programming)
memo_path = os.path.abspath("./memo.npy")
memo = np.load(memo_path).item() if os.path.isfile(memo_path) else {0: 1, 1: 1}


# print("loaded memo=%s" % memo)


def calc_factorials(n):
    """
    Calc n factorial.
    """

    def re_calc_fact(n):
        if n > 2:
            if n not in memo:
                memo[n] = n * re_calc_fact(n - 1)
            return memo[n]
        elif n == 2:
            memo[2] = 2
            return 2

    if n not in memo:
        fact = re_calc_fact(n)
        np.save(memo_path, memo)
    else:
        fact = memo[n]

    return fact


def calc_stirling_approx(n):
    """
    Calc the Striling approximation for n.
    """
    return np.sqrt(2 * np.pi * n) * ((n / np.e) ** n)


if args.n:
    print("%d factorials is %d" %
          (args.n, calc_factorials(args.n)))
    print("And the Stirling approximation is %f" %
          calc_stirling_approx(args.n))
    # print("modified memo=%s" % memo)
else:
    x_stirl = np.arange(0, 6, 0.1)
    y_stirl = calc_stirling_approx(x_stirl)
    x_fact = np.arange(0, 6, 1)
    y_fact = np.array([calc_factorials(i) for i in x_fact])
    plot0, = plt.plot(x_stirl, y_stirl, linewidth=2.)
    plot1, = plt.plot(x_fact, y_fact, "ro")

    plt.legend([plot0, plot1],
               ["Striling approximation", "n!"])
    plt.show()
