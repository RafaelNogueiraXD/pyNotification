import argparse
import logging
parser = argparse.ArgumentParser()
parser.add_argument("Nº ao quadrado", type=int,
                    help="digite um numero para eleva-lo")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="diz alguma coisa")

help_msg = "Logging level (INFO=%d DEBUG=%d)" % (logging.INFO, logging.DEBUG)
	parser.add_argument("--verbosity", "-v", help=help_msg, default=DEFAULT_LOG_LEVEL, type=int)
# configura o mecanismo de logging

args = parser.parse_args()
if args.verbosity == logging.DEBUG:
    #mostra mais detalhes
    logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                        datefmt=TIME_FORMAT, level=args.verbosity)

else:
    logging.basicConfig(format='%(message)s',datefmt=TIME_FORMAT, level=args.verbosity)
answer = args.square**2
if args.verbose:
    print(f"a conta de {args.square} igual {answer}")
else:
    print(answer)