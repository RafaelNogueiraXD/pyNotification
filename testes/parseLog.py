import argparse
import logging

def parse_arguments():
    parser = argparse.ArgumentParser()
    # adiciona argumentos
    parser.add_argument("-v", "--verbose", action="store_true", help="diz alguma coisa")

    help_msg = "Logging level (INFO=%d DEBUG=%d)" % (logging.INFO, logging.DEBUG)

    args = parser.parse_args()
    return args

def configure_logging(verbose):
    if verbose == logging.DEBUG:
        # Mostra mais detalhes
        logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                            level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(message)s', level=verbose)

# def calculate_square(args):
#     answer = args.square**2
#     if args.verbose:
#         print(f"A conta de {args.square} igual {answer}")
#     else:
#         print(answer)

def main():
    args = parse_arguments()
    configure_logging(args.verbose)
    # calculate_square(args)

if __name__ == "__main__":
    main()
