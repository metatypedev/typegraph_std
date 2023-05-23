import argparse
import traceback
import sys
from generators.generator_script import GeneratorScript
from generators.google import Google
from generators.stripe import Stripe
from generators.github import Github

"""
Usage:

Run all generators
    python3 dev/generate.py -v
Run a specific generator
    python3 dev/generate.py -v -g google
"""

parser = argparse.ArgumentParser(
    description="Script generator",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
parser.add_argument("-i", "--init", action="store_true", help="update __init__.py only")
parser.add_argument("-g", "--generator", type=str, help="specify a generator")


cli_args = parser.parse_args()

GeneratorScript._VERBOSE = cli_args.verbose

# generator list
generators = [Stripe(), Google(), Github()]


# flag g
def gfilter(g: GeneratorScript):
    if cli_args.generator is None:
        return True
    name = g.__class__.__name__
    return name.lower() == cli_args.generator.lower()


generators = list(filter(gfilter, generators))

count, total = 1, len(generators)
for generator in generators:
    name = generator.__class__.__name__
    try:
        print(f"[{count}/{total}] Running {name}")
        count += 1
        if cli_args.init:
            generator.update_init_py()
        else:
            generator.run()
        print()
    except Exception as e:
        if cli_args.verbose:
            traceback.print_exception(*sys.exc_info())
        else:
            print(f"{name} generator failed:", e.__str__(), file=sys.stderr)
