from MainScript import *
import customtkinter
from threading import Thread

# Root configuration
customtkinter.set_appearance_mode("System")
customtkinter.set_appearance_mode("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Cryptocurrency Scraper")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# Update scrape data GUI
app.price_frame = customtkinter.CTkFrame(app)
app.price_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
app.price_frame.grid_columnconfigure(0, weight=1)
app.price_frame.grid_rowconfigure(0, weight=1)

crypto_price_display = customtkinter.CTkTextbox(app.price_frame, height=35, width=200, border_spacing=3,
                                                font=("times new roman", 22))
crypto_price_display.grid(row=0, column=0, padx=0, pady=0)


# Price data to GUI
def update_gui():
    while True:
        price = scrape_data()
        crypto_price_display.configure(state="normal")
        crypto_price_display.delete("1.0", "end")
        crypto_price_display.insert("1.0", price)
        app.update()


update_thread = Thread(target=update_gui)
update_thread.daemon = True
update_thread.start()

# Coin type display TODO: Fix display of coin type when selected
app.cointype_frame = customtkinter.CTkFrame(app)
app.cointype_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
app.cointype_frame.grid_columnconfigure(0, weight=1)

coin_type = customtkinter.CTkLabel(app.cointype_frame, textvariable=coin_choice)
coin_type.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

# Buy/Sell Buttons TODO: Finish connecting them with website div
app.buy_sell_button_frame = customtkinter.CTkFrame(app)
app.buy_sell_button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
app.buy_sell_button_frame.grid_columnconfigure(0, weight=1)
app.buy_sell_button_frame.grid_columnconfigure(1, weight=1)

buy_button = customtkinter.CTkButton(app.buy_sell_button_frame, text="Buy")
buy_button.grid(row=0, column=0, padx=(0, 5), pady=10, sticky="ew")

sell_button = customtkinter.CTkButton(app.buy_sell_button_frame, text="Sell")
sell_button.grid(row=0, column=1, padx=(5, 0), pady=10, sticky="ew")

# Select crypto chart
app.button_frame = customtkinter.CTkFrame(app)
app.button_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
app.button_frame.grid_columnconfigure(0, weight=1)

crypto_1 = customtkinter.CTkButton(app.button_frame, text="Bitcoin", command=lambda: update_url("Bitcoin"))
crypto_1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

crypto_2 = customtkinter.CTkButton(app.button_frame, text="Ethereum", command=lambda: update_url("Ethereum"))
crypto_2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

crypto_3 = customtkinter.CTkButton(app.button_frame, text="Lunc", command=lambda: update_url("Lunc"))
crypto_3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")


# Exit program function and button
def exit_program():
    driver.quit()
    app.quit()


app.exit_button = customtkinter.CTkFrame(app)
app.exit_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
app.exit_button.grid_columnconfigure(0, weight=1)

end_process = customtkinter.CTkButton(app.exit_button, text="Exit", command=exit_program)
end_process.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

app.mainloop()
