# добавляем комбобокс с популярными валютами
import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event): # event - потому что возникает, когда происходит ComboboxSelected
    # Получаем полное название валюты из словаря и обновляем метку
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)



def exchange():
    code = combobox.get()


    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']: # код валюты
                exchange_rate = data['rates'][code]
                c_name = cur[code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {c_name} за 1 USD") # .2f - сколько знаков в числе после запятой
            else:
                mb.showerror("Ошибка", f"Неверный код валюты {code}")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Введите код валюты")


cur = {'EUR': 'Евро',
       'RUB':'РФ рубль',
       'CNY': 'Китайский юань',
       'KRW': 'Восточная Корея',
       'JPY': 'Японская иена',
       'GBP': 'Фунт стерлингов',
       'KZT': 'Казахстанский тенге',
       'UZS': 'Узбекский сум',
       'CHF': 'Швейцарский франк',
       'CZK': 'Чешская крона',
       'NZD': 'Новая Зеландия',
       'BRL': 'Бразильский реал',
       'AED': 'Дирхам',
       'TRY': 'Турецкая лира'}

window = Tk()
window.title("Конвертер валют")
window.geometry('400x200')

Label(text="Выберите код валюты").pack(padx=10, pady=10)


combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)


window.mainloop()
