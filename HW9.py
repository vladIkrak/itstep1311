import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox


class CurrencyConverter:
    URL = "https://bank.gov.ua/ua/markets/exchangerates"
    API = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"

    def __init__(self):
        self.rate = self.get_rate()

    def get_rate(self):
        try:
            page = requests.get(self.URL, timeout=10)
            soup = BeautifulSoup(page.text, "html.parser")
            for row in soup.find_all("tr"):
                cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
                if "USD" in cells:
                    return float(cells[-1].replace(",", "."))
        except Exception:
            pass
        data = requests.get(self.API, timeout=10).json()
        return float(data[0]["rate"])

    def uah_to_usd(self, uah):
        return uah / self.rate


def main():
    try:
        converter = CurrencyConverter()
    except Exception:
        messagebox.showerror("Error", "Could not get the exchange rate.\nCheck your internet connection.")
        return

    GREEN_DARK = "#1b5e20"
    GREEN_LIGHT = "#c8e6c9"
    GREEN_BUTTON = "#2e7d32"

    window = tk.Tk()
    window.title("Currency Converter")
    window.geometry("360x280")
    window.configure(bg=GREEN_LIGHT)

    tk.Label(window, text="UAH → USD Converter", font=("Arial", 16, "bold"),
             bg=GREEN_LIGHT, fg=GREEN_DARK).pack(pady=10)

    tk.Label(window, text=f"NBU rate: 1 USD = {converter.rate:.2f} UAH",
             bg=GREEN_LIGHT, fg=GREEN_DARK).pack()

    tk.Label(window, text="Enter amount in hryvnias (UAH):",
             bg=GREEN_LIGHT, fg=GREEN_DARK).pack(pady=(15, 3))
    entry = tk.Entry(window, justify="center", font=("Arial", 12))
    entry.pack()

    result_label = tk.Label(window, text="", font=("Arial", 15, "bold"),
                            bg=GREEN_LIGHT, fg=GREEN_DARK)
    result_label.pack(pady=15)

    def convert():
        text = entry.get().replace(",", ".")
        try:
            uah = float(text)
            if uah < 0:
                raise ValueError
            usd = converter.uah_to_usd(uah)
            result_label.config(text=f"{uah:.2f} UAH = {usd:.2f} USD")
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid positive number.")

    tk.Button(window, text="Convert", command=convert, bg=GREEN_BUTTON, fg="white",
              font=("Arial", 12, "bold"), width=14).pack()

    entry.bind("<Return>", lambda event: convert())
    entry.focus()
    window.mainloop()


main()