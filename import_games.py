import subprocess

def main():

    print("Choose:")
    print("1. Tic Tac Toe")
    print("2. Display N queens Matrix")
    print("3. Display Magic Square")
    
    choice = input("Enter the number of your choice (1/2/3): ")

    if choice == "1":
        subprocess.run(["python","tictac.py"])

    elif choice == "2":
        subprocess.run(["python","nqueens.py"])

    elif choice == "3":
        subprocess.run(["python","magic square.py"])    

if __name__ == "__main__":
    main()    