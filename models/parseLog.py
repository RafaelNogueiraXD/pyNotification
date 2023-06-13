import argparse
import logging

def parse_arguments():
    parser = argparse.ArgumentParser()
    # adiciona argumentos
    parser.add_argument("email" ,type=str , help="Enviar para: origin - teste - exemplo@gmail.com")
    parser.add_argument("-gpt",type=str , help="Usar o auxilio da IA")
    parser.add_argument("-i",type=str , help="Escolher arquivo de entrada")
    parser.add_argument("-o",type=str , help="Escolher arquivo de saida")
    parser.add_argument("-v", "--verbose",action="store_true")
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

def email_identify(args):
    if args.email == "origin":
        return 'leapylab@gmail.com'
    elif args.email == "teste":
        return 'testexe2904@gmail.com'
    else:
        return args.email 
#nao esta pronto, em andamento
def fileOutput(args):
    if args.o:
        return str(args.o)
    else:
        return "/home/rafael/Área de Trabalho/trabalhos/pyNotification/arquivo.zip"
def fileInput(args):
    if args.i:
        return str(args.i)
    else:
        return "/home/rafael/Área de Trabalho/trabalhos/pyNotification/models/bash/execC.sh"
def main():
    args = parse_arguments()
    configure_logging(args.verbose)
    print(email_identify(args))
    print(fileOutput(args))
    print(fileInput(args))
    # calculate_square(args)

if __name__ == "__main__":
    main()
