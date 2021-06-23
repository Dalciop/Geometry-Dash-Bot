import tkinter as tk

class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        fr = tk.Frame(self)
        fr_bot_token = tk.Frame(self)

        self.mute_label = tk.Label(fr, text="MUTE AT:")
        self.mute_entry = tk.Entry(fr)
        self.mute_button = tk.Button(fr, text="Set", command=self.click_mute_button)

        self.notify_on_best_var = tk.IntVar()
        self.notify_on_best_checkbox = tk.Checkbutton(fr, text='Notify on new best',variable=self.notify_on_best_var, onvalue=1, offvalue=0, command=self.notify_on_best)
        
        self.mute_label.grid(row=0, column=0, sticky = "nsew", padx=5, pady=5)
        self.mute_entry.grid(row=1, column=0, sticky = "nsew", padx=5, pady=5)
        self.mute_button.grid(row=2, column=0, sticky = "nsew", padx=5, pady=5)
        self.notify_on_best_checkbox.grid(row=0, column=1, sticky = "nsew", padx=5, pady=5)

        self.bot_token_label = tk.Label(fr_bot_token, text="DISCORD BOT TOKEN")
        self.bot_token_entry = tk.Entry(fr_bot_token, width=70)
        self.bot_token_button = tk.Button(fr_bot_token, text="Set", command=self.click_bot_token_button)

        self.bot_token_label.grid(row=0, column=0, sticky = "nsew", padx=5, pady=5)
        self.bot_token_entry.grid(row=1, column=0, sticky = "nsew", padx=5, pady=5)
        self.bot_token_button.grid(row=2, column=0, sticky = "nsew", padx=5, pady=5)
        
        fr.grid(row=0, column=0, sticky="ns")
        fr_bot_token.grid(row=1, column=0, sticky="ne")


    def click_bot_token_button(self):
        f = open("TOKEN.token", "w")
        f.write(self.bot_token_entry.get())
        self.bot_token_entry.delete(0, tk.END)

    def notify_on_best(self):
        if (self.notify_on_best_var.get() == 1):
            f = open("preferences.conf", "w")
            f.write(self.notify_on_best_var.get())

    def click_mute_button(self):
        f = open("mute.value", "w")
        f.write(self.mute_entry.get())

w = SampleApp()
w.title("Geometry Dash Bot")
w.mainloop()