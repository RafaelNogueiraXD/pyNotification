import subprocess
import shlex, subprocess
command_line = input()
# /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
# args = shlex.split(command_line)
# print(args)
# ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
# p = subprocess.Popen(command_line) # Success!
# Executa o comando "ls" em um terminal e captura a saída em uma variável
# output = subprocess.check_output(["ls"])
print(command_line.encode())
