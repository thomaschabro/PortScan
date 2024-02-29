import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports(target, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            open_ports.append(port)
        
        sock.close()
    
    return open_ports

def scan_ports_and_display():
    target = entry_target.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())
    
    open_ports = scan_ports(target, start_port, end_port)
    
    if open_ports:
        for open_port in open_ports:
            result_text.set(f"Porta [ {open_port} ] aberta em {target} : {socket.getservbyport(open_port)} \n")
    else:
        result_text.set(f"Nenhuma porta aberta encontrada em {target}.")

# Criar a interface gráfica
app = tk.Tk()
app.title("Scanner de Portas")

# Componentes da interface
label_target = tk.Label(app, text="Endereço IP do destino:")
entry_target = tk.Entry(app)

label_start_port = tk.Label(app, text="Porta inicial:")
entry_start_port = tk.Entry(app)

label_end_port = tk.Label(app, text="Porta final:")
entry_end_port = tk.Entry(app)

scan_button = tk.Button(app, text="Escanear", command=scan_ports_and_display)

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text)

# Posicionamento dos componentes
label_target.pack()
entry_target.pack()

label_start_port.pack()
entry_start_port.pack()

label_end_port.pack()
entry_end_port.pack()

scan_button.pack()

result_label.pack()

# Iniciar o loop principal da interface gráfica
app.mainloop()