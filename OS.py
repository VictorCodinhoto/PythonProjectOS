import os
import signal
import sys
import platform

#Integrantes
#João Antonnio Martinez - 23.00983-7
#Victor Codinhoto Batista - 23.00051-0
#Carlos Antonio dos santos Roth Gorham - 24.95009-2
#Daniel Djinishian de Briquez - 22.00251-0

def fork_process():
    pid = os.fork()
    if pid == 0:
        print(f"Processo filho (PID: {os.getpid()})")
        os._exit(0)
    else:
        print(f"Processo pai (PID: {os.getpid()}) criou o filho (PID: {pid})")
        pid_filho, status = os.wait()
        print(f"Filho (PID: {pid_filho}) terminou com status: {status}")

def execute_command(command):
    # Verifica o sistema operacional
    if platform.system() == "Windows" and command == "ls -l":
        command = "dir"  # Substitui 'ls -l' por 'dir' no Windows
    resultado = os.system(command)
    print(f"Código de saída: {resultado}")

def execute_spawn(command):
        os.spawnl(os.P_NOWAIT, "/bin/ls", "ls", "-l")

def kill_process(pid):
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"Processo {pid} encerrado com sucesso.")
    except ProcessLookupError:
        print(f"Processo {pid} não encontrado.")
    except Exception as e:
        print(f"Erro ao encerrar o processo: {e}")

def show_process_info():
    print(f"PID do processo atual: {os.getpid()}")
    print(f"PGID do processo atual: {os.getpgid(0)}")
    print(f"UID do processo atual: {os.getuid()}")
    print(f"GID do processo atual: {os.getgid()}")

def replace_process():
    os.execl("/bin/ls", "ls", "-l")

def main():
    while True:
        try:
            command = input("shell> ")
            if command in ('exit', 'quit'):
                print("Saindo do interpretador...")
                break
            elif command == 'fork':
                fork_process()
            elif command.startswith('exec '):
                execute_command(command[5:].strip())
            elif command == 'spawn':
                execute_spawn("ls -l")
            elif command.startswith('kill '):
                pid = int(command.split()[1])
                kill_process(pid)
            elif command == 'info':
                show_process_info()
            elif command == 'replace':
                replace_process()
            else:
                execute_command(command)
        except KeyboardInterrupt:
            print("\nSaindo...")
            sys.exit(0)
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
