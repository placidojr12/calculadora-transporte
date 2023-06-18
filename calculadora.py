import calendar
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calcular_gasto_passagens(valor_passagem_onibus, valor_passagem_ferry, valor_transporte_ferry, dias_utilizados_ferry, dias_utilizados_transporte, dias_utilizados_onibus):
    dias_uteis = obter_dias_uteis()
    gasto_semanal = 0
    
    if dias_utilizados_onibus > 0:
        gasto_semanal += (valor_passagem_onibus * 2) * dias_utilizados_onibus
    
    if dias_utilizados_ferry > 0:
        gasto_semanal += (valor_passagem_ferry + valor_transporte_ferry) * dias_utilizados_ferry
    
    gasto_mensal = gasto_semanal * 4  # Multiplica o gasto semanal por 4 semanas
    return gasto_semanal, gasto_mensal

def obter_dias_uteis():
    dias_uteis = 0
    ano = datetime.date.today().year
    mes = datetime.date.today().month
    _, num_dias = calendar.monthrange(ano, mes)
    for dia in range(1, num_dias + 1):
        if calendar.weekday(ano, mes, dia) < 5:
            dias_uteis += 1
    return dias_uteis

def exibir_resultado():
    try:
        valor_passagem_onibus = float(valor_passagem_onibus_entry.get())
        valor_passagem_ferry = float(valor_passagem_ferry_entry.get())
        valor_transporte_ferry = float(valor_transporte_ferry_entry.get())
        dias_utilizados_ferry = int(dias_utilizados_ferry_entry.get())
        dias_utilizados_transporte = int(dias_utilizados_transporte_entry.get())
        dias_utilizados_onibus = int(dias_utilizados_onibus_entry.get())
        
        gasto_semanal, gasto_mensal = calcular_gasto_passagens(valor_passagem_onibus, valor_passagem_ferry, valor_transporte_ferry, dias_utilizados_ferry, dias_utilizados_transporte, dias_utilizados_onibus)
        
        resultado_window = tk.Toplevel()
        resultado_window.title("Resultado")
        resultado_window.configure(bg="#f0f0f0")
        
        resultado_semanal_label = ttk.Label(resultado_window, text=f"Gasto semanal: R$ {gasto_semanal:.2f}", font=("Arial", 14, "bold"), background="#f0f0f0")
        resultado_mensal_label = ttk.Label(resultado_window, text=f"Gasto mensal: R$ {gasto_mensal:.2f}", font=("Arial", 14, "bold"), background="#f0f0f0")
        
        resultado_semanal_label.pack(pady=10, padx=10)
        resultado_mensal_label.pack(pady=10, padx=10)
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite valores numéricos válidos.")

window = tk.Tk()
window.title("Calculadora de Gastos com Passagens")
window.configure(bg="#f0f0f0")
window.geometry("400x450")

titulo_label = ttk.Label(window, text="Calculadora de Gastos", font=("Arial", 16, "bold"), background="#f0f0f0")
valor_passagem_onibus_label = ttk.Label(window, text="Valor da passagem de ônibus (ida e volta): R$", font=("Arial", 12), background="#f0f0f0")
valor_passagem_onibus_entry = ttk.Entry(window, font=("Arial", 12))
valor_passagem_ferry_label = ttk.Label(window, text="Valor da passagem de ferry (ida e volta): R$", font=("Arial", 12), background="#f0f0f0")
valor_passagem_ferry_entry = ttk.Entry(window, font=("Arial", 12))
valor_transporte_ferry_label = ttk.Label(window, text="Valor do transporte até o ferry (ida e volta): R$", font=("Arial", 12), background="#f0f0f0")
valor_transporte_ferry_entry = ttk.Entry(window, font=("Arial", 12))
dias_utilizados_ferry_label = ttk.Label(window, text="Dias da semana utilizados no ferry:", font=("Arial", 12), background="#f0f0f0")
dias_utilizados_ferry_entry = ttk.Entry(window, font=("Arial", 12))
dias_utilizados_transporte_label = ttk.Label(window, text="Dias da semana utilizados no transporte até o ferry:", font=("Arial", 12), background="#f0f0f0")
dias_utilizados_transporte_entry = ttk.Entry(window, font=("Arial", 12))
dias_utilizados_onibus_label = ttk.Label(window, text="Dias da semana utilizados no ônibus (ida e volta):", font=("Arial", 12), background="#f0f0f0")
dias_utilizados_onibus_entry = ttk.Entry(window, font=("Arial", 12))
calcular_button = ttk.Button(window, text="Calcular", command=exibir_resultado, style="Custom.TButton")

titulo_label.pack(pady=10, padx=10)
valor_passagem_onibus_label.pack(pady=10, padx=10)
valor_passagem_onibus_entry.pack(padx=10)
valor_passagem_ferry_label.pack(pady=5, padx=10)
valor_passagem_ferry_entry.pack(padx=10)
valor_transporte_ferry_label.pack(pady=5, padx=10)
valor_transporte_ferry_entry.pack(padx=10)
dias_utilizados_ferry_label.pack(pady=5, padx=10)
dias_utilizados_ferry_entry.pack(padx=10)
dias_utilizados_transporte_label.pack(pady=5, padx=10)
dias_utilizados_transporte_entry.pack(padx=10)
dias_utilizados_onibus_label.pack(pady=5, padx=10)
dias_utilizados_onibus_entry.pack(padx=10)
calcular_button.pack(pady=(20, 10), padx=10)

style = ttk.Style()
style.configure("Custom.TButton", foreground="white", background="#FF7F00", font=("Arial", 12))

window.mainloop()

