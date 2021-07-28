import argparse
import sys

import set01
import set02


parser = argparse.ArgumentParser(
    description="Select specific set and challenge numbers"
)
challenges = parser.add_argument_group("challenges")
challenges.add_argument("-s", metavar="set", type=int, help="set number")
challenges.add_argument("-c", metavar="challenge", type=int, help="challenge number")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.s is None and args.c is not None:
        print(
            "To pass the number of the challenge, you must pass the number of the set"
        )
        sys.exit(1)
    elif args.s is not None and args.c is None:
        if args.s == 1:
            set01.challenges()
        elif args.s == 2:
            set02.challenges()
    elif args.s is not None and args.c is not None:
        if args.s == 1:
            set01.challenges(args.c)
        elif args.s == 2:
            set02.challenges(args.c)
    elif args.s is None and args.c is None:
        set01.challenges()
        set02.challenges()
