def change():
    expense = 23.75
    money = 100
    expense = float(input("Ingresar gasto: "))  
    money = float(input("Dinero recibido: "))   
    change = money - expense   
    pesos = int(change)
    centavos = int((change - pesos) * 100)      
    print("\nVuelto")
    print(f"\nPesos: {pesos}")
    print(f"Centavos: {centavos}")
