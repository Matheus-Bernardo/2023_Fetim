import serial



try:
    conectado = serial.Serial("COM3",115200, timeout= 0.5)
    #print(conectado)
    print("conectado com a porta ", conectado.portstr)

except serial.SerialException:    
    print("nao encontrado nenhuma porta")
    pass

while True:
    comando = input("digite L OU D: ")

    if comando == "L":
        conectado.write(b'1')
    else:
        conectado.write(b'0')
    if input("Deseja continuar?").upper() == "N":
        break

conectado.close
print("Conexão fechada")    
