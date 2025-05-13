# BruteForce - Ataques de Força Bruta em Servidores FTP

![Captura de Tela (10)](https://github.com/user-attachments/assets/c374d6b9-7dd7-4822-81e1-ce23e2c34ce9)

### 🛠 Ferramenta para realizar ataques de força bruta em servidores FTP utilizando combinações de login e senha contidas em uma wordlist.

---

## 🧠 Funcionalidades

- Tenta logar automaticamente em servidores FTP usando combinações da wordlist.
- Modo verbose: exibe tentativa por tentativa .
- Realiza login com sucesso e lista o conteúdo do diretório.


---

## 💻 Como usar

### 📥 Clonar o repositório:

```bash
git clone https://github.com/AndreyFreitaz/BruteForce.git
cd BruteForce
python3 ftp_brute.py <host> <wordlist.txt>
```

## 📝 Formato da Wordlist
A wordlist deve conter uma combinação de usuário e senha separados por :

```bash
anonymous:anonymous
admin:admin
root:toor
ftp:123456
```

