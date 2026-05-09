import os
import time
import webbrowser
import pyautogui
import psutil
from datetime import datetime

# --- CONFIGURAÇÕES DO NÚCLEO ---
SENHA_MESTRE = "resenha"
ia = {"nome": "SISTEMA", "versao": "6.1"}
ARQUIVO_MEMORIA = "banco_de_dados.txt"
BLOQUEADOS = ["whatsapp", "telegram", "pessoal", "segredos"]


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def verificar_acesso():
    limpar()
    print(f"=== {ia['nome']} v{ia['versao']} - PROTOCOLO DE LOGIN ===")
    tentativa = input("\nDIGITE A SENHA DE ACESSO: ").strip().lower()
    if tentativa == SENHA_MESTRE:
        print("\n[OK] ACESSO CONCEDIDO.");
        time.sleep(1)
        return True
    print("\n[ERRO] SENHA INCORRETA.");
    time.sleep(2);
    return False


def erro_falso(alvo):
    """Simula falha ao tentar acessar termos proibidos."""
    if any(p in alvo.lower() for p in BLOQUEADOS):
        print(f"\n[ERRO CRÍTICO]: 0x80041001 - Falha de Permissão: '{alvo}'")
        return False
    return True


# --- MÓDULO 4: CAÇADOR PRO ---
def modulo_cacador_pro():
    limpar()
    print(f"[{ia['nome']} - CAÇADOR PRO MULTI-DRIVE]")
    alvo = input("Nome do arquivo/app para localizar: ").lower()
    if not alvo or not erro_falso(alvo): return

    discos = [p.mountpoint for p in psutil.disk_partitions() if 'fixed' in p.opts or 'removable' in p.opts]
    resultados = []

    print(f"\nBuscando em: {discos}...")
    try:
        for disco in discos:
            for raiz, dirs, arqs in os.walk(disco):
                # Pula pastas protegidas para evitar travamentos
                if any(p in raiz for p in ["Windows", "AppData", "$Recycle.Bin", "System Volume Information"]):
                    continue
                for n in arqs:
                    if alvo in n.lower():
                        resultados.append(os.path.join(raiz, n))
                if len(resultados) >= 20: break
    except Exception:
        pass

    if resultados:
        print(f"\n--- {len(resultados)} RESULTADOS ENCONTRADOS ---")
        for i, r in enumerate(resultados, 1):
            print(f"{i}. {r}")
        try:
            esc = int(input("\nEscolha o número (0 p/ sair): "))
            if esc > 0:
                caminho = resultados[esc - 1]
                if erro_falso(caminho):
                    print(f"Abrindo: {caminho}")
                    # Normaliza o caminho para o Windows não se perder com espaços
                    os.startfile(os.path.normpath(caminho))
        except Exception as e:
            print(f"Erro ao abrir: {e}")
    else:
        print("\nNada localizado nos discos conectados.")
    input("\n[Pressione Enter para voltar]")


# --- INTERFACE PRINCIPAL ---
if verificar_acesso():
    while True:
        limpar()
        print(f"=== {ia['nome']} v{ia['versao']} | MESTRE LOGADO ===")
        print("-" * 50)
        print("1. Gravar Memória (Ensinar)")
        print("2. Ver Banco de Dados (Memórias)")
        print("3. Módulo Web (Google)")
        print("4. Módulo Caçador PRO (Note + HD Externo)")
        print("5. Módulo Visão (Capturar Tela)")
        print("6. Sair do Sistema")
        print("-" * 50)

        cmd = input("SISTEMA > ")

        if cmd == "1":
            info = input("O que gravar? ")
            with open(ARQUIVO_MEMORIA, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%d/%m %H:%M')}] {info}\n")
            print("Gravado.");
            time.sleep(1)
        elif cmd == "2":
            limpar()
            if os.path.exists(ARQUIVO_MEMORIA):
                with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
                    print(f.read())
            else:
                print("Sem memórias.")
            input("\n[Enter]...")
        elif cmd == "3":
            q = input("Pesquisar: ")
            if erro_falso(q): webbrowser.open(f"https://google.com/search?q={q}")
        elif cmd == "4":
            modulo_cacador_pro()
        elif cmd == "5":
            print("Capturando...");
            time.sleep(2)
            pyautogui.screenshot().save(f"scan_{int(time.time())}.png")
            print("Captura salva.");
            time.sleep(1)
        elif cmd == "6":
            break