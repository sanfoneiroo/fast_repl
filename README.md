# fast-repl ESP32 (MicroPython)

##  Descrição

O **fast-repl** é um `main.py` pensado para acelerar meus estudos com **MicroPython no ESP32**, aproveitando ao máximo o uso do **REPL** (Read–Eval–Print Loop). A ideia é ter, logo na inicialização do microcontrolador, um ambiente pronto para experimentação, com: Bibliotecas mais usadas já importadas; Funções utilitárias definidas; Wi‑Fi ativado; Interface simples de boas‑vindas no shell

Assim, consigo testar ideias, sensores e atuadores sem precisar escrever, compilar e subir um código completo a cada experimento, como acontece no fluxo tradicional da Arduino IDE.

##  Motivação

Após instalar o firmware do MicroPython no ESP32, conheci o REPL, que permite interpretar comandos e códigos em tempo real via shell (uso principalmente pelo Thonny).

Esse fluxo mudou bastante minha forma de estudar microcontroladores com resposta imediata aos comando, experimentação interativa,e xploração de módulos com dir() e aprendizado mais próximo do funcionamento real do hardware

##  O que este código faz

Ao iniciar o ESP32:  
Importa automaticamente:  
machine   
Pin  
time  
network  
ntptime  
* Ativa a interface Wi‑Fi em modo station
* Exibe um painel inicial com comandos disponíveis
* Disponibiliza funções utilitárias no REPL

(Existe também um sistema simples de senha para travar o acesso ao REPL, atualmente comentado, que deve ser aprimorado no futuro, oferencendo segurança ao hardware)


##  Estrutura

```text
main.py   # fast-repl
```

Basta copiar o arquivo para o ESP32 como `main.py`.


## Painel inicial

Ao iniciar, o REPL exibe as bibliotecas já carregadas, funções disponíveis e mensagem de confirmação do shell ativo

Isso ajuda a saber imediatamente em que estado o sistema está.


## Funções disponíveis

### `conectar_wifi(SSID, password)`

Conecta o ESP32 a uma rede Wi‑Fi.

```python
conectar_wifi("MinhaRede", "MinhaSenha")
```

Retorna `True` ou `False` dependendo do status da conexão.

---

### `info_wifi()`

Exibe as informações de rede (IP, gateway, DNS, etc.).

```python
info_wifi()
```

---

### `atualizar_hora(fuso)`

Sincroniza o relógio interno via NTP e ajusta o fuso horário.

```python
atualizar_hora(-3)  # Brasil
```


##  Observação

Este projeto é um laboratório pessoal de estudos, mas pode ser útil para qualquer pessoa que esteja começando (ou aprofundando) o uso de MicroPython com ESP32.

Sinta‑se à vontade para adaptar, melhorar e experimentar.