# ChatBot simples

# -----------------------------
# Versão antiga (COMENTAR)
# -----------------------------
"""
nome = input("Qual é o seu nome? ")
print(f"Olá {nome}, tudo bem?")
idade = int(input("Quantos anos tens? "))

if idade < 18:
    print("És menor de idade!")
else:
    print("És maior de idade!")

print("Obrigado por usares o chatbot!")
"""

# -----------------------------
# Versão nova (DESCOMENTADA)
# -----------------------------

print("Olá! Eu sou o ChatBot. Escreve 'sair' para terminar.\n")

while True:
    mensagem = input("Tu: ").lower()

    if mensagem == "sair":
        print("ChatBot: Até à próxima!")
        break

    # Interações originais
    if mensagem == "ola" or mensagem == "olá":
        print("ChatBot: Olá! Como estás?")
    elif mensagem == "tudo bem":
        print("ChatBot: Que bom! Como posso ajudar?")
    elif mensagem == "qual é o teu nome":
        print("ChatBot: Eu sou o ChatBot criado pelo Diogo!")
    
    # -----------------------------
    # 5 NOVAS INTERAÇÕES PEDIDAS
    # -----------------------------
    elif mensagem == "que horas são":
        import datetime
        agora = datetime.datetime.now().strftime("%H:%M")
        print(f"ChatBot: Agora são {agora}.")

    elif mensagem == "quem te criou":
        print("ChatBot: Fui criado pelo Diogo como parte do exercício do stor!")

    
