"""
How many people do we need to have in a room to make it a favorable bet
(probability of success greater than 1/2) that two people in the room
will have the same birthday?
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(
    description="The permutation generator for solving the problem: How many "
                "people do we need to have in a room to make it a favorable "
                "bet (probability of success greater than 1/2) that two "
                "people in the room will have the same birthday?")
parser.add_argument("-n", type=int,
                    help="The amount of people in a room.")
args = parser.parse_args()


def calc_prob(ppl_num):
    """
    Calc the probability of that ppl have no duplication of birthdays.
    """
    prob_no_dup = 1
    if ppl_num > 1:
        for i in range(1, ppl_num):
            prob_no_dup *= (365. - i if i <= 365 else 0) / 365.
    return 1. - prob_no_dup

if args.n:
    print(parser.description)
    print("Probability of %d ppl having the same birthday is %f" %
          (args.n, calc_prob(args.n)))
else:
    x = np.arange(1, 365 + 1, 1)
    y0 = np.array([calc_prob(i) for i in x])
    y1 = 1. - y0
    plot0, = plt.plot(x, y0, linewidth=2.)
    plot1, = plt.plot(x, y1, linewidth=2.)

    plt.legend([plot0, plot1],
               ["same birthday", "no duplications of birthday"])
    plt.show()

