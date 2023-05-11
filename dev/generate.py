import argparse
import traceback
import sys
from generators.google import Google

"""
Usage:

Run all generators
    python3 dev/generate.py -v
Run a specific generator
    python3 dev/generate.py -v -g google
"""

parser = argparse.ArgumentParser(
    description="Script generator",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="verbose output"
)

parser.add_argument(
    "-g",
    "--generator",
    type=str,
    help="specify a generator"
)


cli_args = parser.parse_args()

generators = [
    Google()
]

count, total = 1, len(generators)
for generator in generators:
    name = generator.__class__.__name__
    if cli_args.generator is not None:
        if name.lower() != cli_args.generator.lower():
            continue
    try:
        print(f"[{count}/{total}] Running {name}")
        count += 1
        generator.run()
    except Exception as e:
        if cli_args.verbose:
            traceback.print_exception(*sys.exc_info())
        else:
            print(f'{name} generator failed:', e.__str__())
