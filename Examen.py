import tkinter as tk
import random
numero_secreto = random.randint(0, 100)
def verificar_numero():
 intento = int(entrada.get())
 if intento < numero_secreto:
     mensaje.set("El número es mayor ⬆")
 elif intento > numero_secreto:
    mensaje.set("El número es menor ⬇")
 else:
     mensaje.set("¡Felicidades! 🎉 Has adivinado el número.")
 boton_reiniciar.pack()
def reiniciar_juego():
 global numero_secreto
 numero_secreto = random.randint(0, 100)
 mensaje.set("Intenta adivinar el número entre 0 y 100")
 entrada.delete(0, tk.END)
 boton_reiniciar.pack_forget()
ventana = tk.Tk()
ventana.title("Adivina el Número")
ventana.geometry("400x300")
tk.Label(ventana, text="Introduce un número del 0 al 100:").pack()
entrada = tk.Entry(ventana)
entrada.pack()
boton_verificar = tk.Button(ventana, text="Comprobar", command=verificar_numero)
boton_verificar.pack()
mensaje = tk.StringVar()
mensaje.set("Intenta adivinar el número entre 0 y 100")
etiqueta_mensaje = tk.Label(ventana, textvariable=mensaje)
etiqueta_mensaje.pack()
boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
ventana.mainloop()
