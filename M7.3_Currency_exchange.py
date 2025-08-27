# добавляем комбобокс с популярными валютами
import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_t_label(event):  # event - потому что возникает, когда происходит ComboboxSelected
    # Получаем полное название валюты из словаря и обновляем метку
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def update_b_label(event):  # event - потому что возникает, когда происходит ComboboxSelected
    # Получаем название базовой валюты из словаря и обновляем метку
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()
            if t_code in data['rates']:  # код валюты
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена",
                            f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")  # .2f - сколько знаков в числе после запятой
            else:
                mb.showerror("Ошибка", f"Неверный код валюты {t_code}")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Введите код валюты")


cur = {'EUR': 'Евро',
       'USD': 'Доллар США',
       'RUB': 'РФ рубль',
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
window.geometry('400x300')

Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)

t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
