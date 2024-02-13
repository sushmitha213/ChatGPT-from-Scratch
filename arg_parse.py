import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='This is a demonstration program')

    # Here we add an argument to the parser, specifying the expecteed type, a help message, etc
    parser.add_argument('-llms',type=str,required=True,help='Please provide an llms')

    return parser.parse_args()

def main():
    args = parse_args()

    # Now we can use the argument value in our program.
    print(f'The provided llms is: {args.llms}')

if __name__ == '__main__':
    main()