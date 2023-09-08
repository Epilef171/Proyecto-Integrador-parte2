import readchar

def main():
    print("Presiona la tecla UP para salir.")

    while True:
        char = readchar.readkey()
        if char == "\x00H":  
            print("Tecla UP presionada. Saliendo del programa.")
            break
        else:
            print(f"Tecla presionada: {char}")

if __name__ == "__main__":
    main()
