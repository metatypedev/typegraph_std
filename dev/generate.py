import argparse
from generators.google import Google

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


cli_args = parser.parse_args()

generators = [
    Google()
]

for generator in generators:
    name = generator.__class__.__name__
    try:
        print(f"Running {name}")
        generator.run()
    except Exception as e:
        print(f'Generator "{name}" failed')
        if cli_args.verbosity:
            print(e.__str__())
