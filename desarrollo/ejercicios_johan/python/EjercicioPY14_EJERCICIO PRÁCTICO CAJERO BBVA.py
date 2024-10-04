print("\t Cajero Automático BBVA \n")
pinC, saldo, valRagua, valRluz, valRgas, valRinter = 1222, 500000, 10000, 29000, 3500, 90000

inserTar = input("Insertar tarjeta(s/n): ")

while inserTar.lower() != 's':
    print("\n ¡PARA CONTINUAR DEBE INSERTAR LA TARJETA!")
    inserTar = input("Insertar tarjeta(s/n): ")

contPin = 0 
pin = int(input("\n Ingrese su PIN pára continuar: "))

while pin != pinC:
    contPin += 1
    
    if contPin > 3:
        print("\n ¡ADVERTENCIA! Sólo tiene 1 intento más")
        pin = int(input("Ingrese su PIN para continuar: "))

        if contPin > 1:
            print("\n ¡DEMASIADOS INTENTOS FALLIDOS, INTÉNTELO MÁS TARDE!")
            break

    print("\n ¡PIN INCORRECTO!")
    pin = int(input("Ingrese su PIN para continuar: "))

if pin == pinC:
    print("\n Elija el tipo de transacción que desea realizar:")

    print("\n 1. Para Retiro de Dinero \n 2. Para Consulta de Saldo \n 3. Para Pago de Recibos Públicos \n 4. Transferencia a otra Cuenta \n")
    transTyp = int(input("Ingrese el número de la transacción a realizar: "))

    while transTyp <= 0 or transTyp > 4:
        transTyp = int(input("Ingrese un número VÁLIDO para la transacción a realizar: "))

    match transTyp:
        case 1:
            print("\n PARA RETIRAR DINERO:\n")
            cantRet = int(input("Ingrese la cantidad que desea retirar: "))
            confirm = input(f"¿Desea retirar ${cantRet} de su cuenta? (s/n): ")
                
            while confirm.lower() != 's':
                cantRet = int(input("Entonces ingrese la cantidad que desea retirar: "))
                confirm = input(f"¿Desea retirar ${cantRet} de su cuenta? (s/n): ")

            if confirm.lower() == 's':
                print("\t\n...RETIRANDO DINERO...\n")
                saldoFinal = saldo - cantRet
                resImp = input("¿Desea Imprimir su saldo restante en la pantalla? (s/n): ")
                    
                if resImp.lower() == 's':
                    print(f"\n EL SALDO RESTANTE EN SU CUENTA ES DE $ {saldoFinal} \n")
             
        case 2:
            print("\n PARA CONSULTAR SALDO:\n")
            print(f"Su saldo actual es de: $ {saldo}")
            
        case 3:
            print("\n PARA PAGO DE RECIBOS PÚBLICOS:\n")
            print("1. Recibo de Agua \n 2. Recibo de Luz \n 3. Recibo de Gas \n 4. Recibo de Internet \n")
            recEleg = int(input("Ingrese el número del recibo que desea pagar: "))

            while recEleg <= 0 or recEleg > 4:
                recEleg = int(input("Ingrese un número VÁLIDO para el recibo a pagar: "))
                    
            if recEleg == 1:
                recibo = 'Agua'
                valPagar = valRagua
            elif recEleg == 2:
                recibo = 'Luz'
                valPagar = valRluz
            elif recEleg == 3:
                recibo = 'Gas'
                valPagar = valRgas
            elif recEleg == 4:
                recibo = 'Internet'
                valPagar = valRinter
                
            print(f"El total a pagar del recibo de {recibo} es de $ {valPagar}")
            confirm = input("\n¿Desea realizar el pago? (s/n): ")

            while confirm != 's':
                recEleg = int(input("Ingrese el número de OTRO recibo que desee pagar: "))
                confirm = input("\n¿Desea realizar el pago? (s/n): ")
                
            if confirm.lower() == 's':
                print("\t\n...REALIZANDO EL PAGO...\n")
                saldoFinal = saldo - valPagar
                resImp = input("¿Desea Imprimir su saldo restante en la pantalla? (s/n): ")
                    
                if resImp.lower() == 's':
                    print(f"\n EL SALDO RESTANTE EN SU CUENTA ES DE $ {saldoFinal} \n")
                    
            
        case 4:
            print("44")
   
    print("FIN DE LA TRANSACCIÓN")
















        






    
