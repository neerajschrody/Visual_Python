import argparse

parser = argparse.ArgumentParser(description="Process SomeE integers")
parser.add_argument('integers', meravar = 'N', type= int, nargs= '+',
                    help = 'an integer ofr accumulator')
L