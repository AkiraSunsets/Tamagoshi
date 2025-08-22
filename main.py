from tamagoshi import Tamagoshi
from bichinhos import Hamster, Cachorro, Gato

def main():
    print("₊⊹Seja bem vindo ao Tamagoshi, seu bichinho virtual₍ᐢ. .ᐢ₎ ₊˚⊹♡")
    print("Loading...")
    nomeUser = input("Qual o seu nome?? \n")
    print("Loading...")
    print("Que nome lindo!!")
    print("Loading...")
    nome = input("Qual o nome do seu bichinho? \n")
 
    print("\nEscolha uma raça para o seu bichinho:")
    print("1 - Gato ")
    print("2 - Cachorro ")
    print("3 - Hamster ")
    escolha = input("Escolha uma opção de 1 a 3: ")
 
    if escolha == "1":
        bicho = Gato(nome)
    elif escolha == "2":
        bicho = Cachorro(nome)
    elif escolha == "3":
        bicho = Hamster(nome)
    else:
        print("Opção inválida, seu bichinho será um Tamagoshi padrão.")
        bicho = Tamagoshi(nome)
 
    # Loop do jogo
    while True:
        print("\n=== MENU ===")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Ver humor")
        print("4 - Ação especial")
        print("5 - Sair")
        print("6 - Ver Status")
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            bicho.alimentar(30)
            print(f"{bicho.nome} foi alimentado!")
        elif opcao == "2":
            bicho.brincar(30)
            print(f"{bicho.nome} brincou e está mais feliz!")
        elif opcao == "3":
            print(f"Humor de {bicho.nome}: {bicho.getHumor()}")
        elif opcao == "4":
            # Submenu para habilidades especiais
            if isinstance(bicho, Hamster):
                print("\nAções especiais do Hamster:")
                print("1 - Rodar na rodinha")
                print("2 - Fazer fofura")
                print("3 - Descansar")
                escolha_esp = input("Escolha: ")
                if escolha_esp == "1":
                    bicho.rodar()
                elif escolha_esp == "2":
                    bicho.fazer_fofura()
                elif escolha_esp == "3":
                    bicho.descansar()
                else:
                    print("Opção inválida!")

            elif isinstance(bicho, Cachorro):
                print("\nAções especiais do Cachorro:")
                print("1 - Latir")
                print("2 - Correr")
                print("3 - Receber carinho")
                escolha_esp = input("Escolha: ")
                if escolha_esp == "1":
                    bicho.latir()
                elif escolha_esp == "2":
                    bicho.correr()
                elif escolha_esp == "3":
                    bicho.receber_carinho()
                else:
                    print("Opção inválida!")

            elif isinstance(bicho, Gato):
                print("\nAções especiais do Gato:")
                print("1 - Miar")
                print("2 - Dormir")
                print("3 - Arranhar")
                escolha_esp = input("Escolha: ")
                if escolha_esp == "1":
                    bicho.miar()
                elif escolha_esp == "2":
                    bicho.dormir()
                elif escolha_esp == "3":
                    bicho.arranhar()
                else:
                    print("Opção inválida!")

            else:
                print(f"{bicho.nome} não tem habilidades especiais.")
        elif opcao == "5":
            print(f"{bicho.nome} está indo dormir... Até logo! 😴")
            break
        
        elif opcao == "6":
            print(f"\n📊 Status de {bicho.nome}:")
            print(f"Idade: {round(bicho.idade, 1)} anos")
            print(f"Saúde: {bicho.saude}")
            print(f"Fome: {bicho.fome}")
            print(f"Tédio: {bicho.tedio}")
        else:
            print("Opção inválida!")

        bicho.tempoPassando()
        
        if bicho.saude <= 0:
            print(f"{bicho.nome} morreu...")
            break
 
if __name__ == "__main__":
    main()
