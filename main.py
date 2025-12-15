# importar bibliotecas
import machine
from machine import Pin
import time
import network
import ntptime

""login de acesso ao fast-repl
travado = True
senha = "admin"
def verificar_senha():
    global travado
    while travado == True:
        try:
            entrada = input("digite  a senha para iniciar o REPL \n")
            if entrada == senha:
                travado = False
            else:
                print("senha inválida")
        except:
            machine.reset()
"""        


#painel
verificar_senha()
print("\n")
print("-----bem vindo ao fast-repl esp32----")
print("--------------------------------")
print ("bibliotecas importadas: machine")
print ("                        Pin;")
print ("                        time;")
print ("                        network;")
print ("                        ntptime;")
print("comandos disponíves: conectar_wifi(SSID, password)")
print("                     info_wifi()")
print("                     help()")
print("                     atualizar_hora(fuso)")
print ("--------------------------------")
print ("---------shell iniciado---------")
print("\n")

# ativar wifi
sta_if = network.WLAN(network.WLAN.IF_STA); sta_if.active(True)

# funcões
def conectar_wifi(SSID, password):
    sta_if.connect(SSID, password)
    print("Conectado?")
    return sta_if.isconnected()
def info_wifi():
    sta_if.ifconfig()
def atualizar_hora(fuso):
    try:
        ntptime.settime()
        print("Hora sincronizada via NTP")
        print(time.localtime(time.time() +fuso * 3600))
    except:
        print("Falha ao sincronizar NTP")