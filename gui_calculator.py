import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Configure the root window's style
        self.root.configure(bg='lightgrey')
        
        self.result_var = tk.StringVar()
        self.create_widgets()
        
        # Bind keyboard events
        self.root.bind('<Key>', self.on_keypress)
        
    def create_widgets(self):
        # Entry for showing the result
        entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), bd=8, insertwidth=4, width=15, borderwidth=4, justify='right', bg='white', fg='black')
        entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Define button styles
        button_style = {'padx': 20, 'pady': 20, 'font': ("Arial", 16), 'bg': '#f0f0f0', 'relief': 'ridge', 'bd': 1}
        button_colors = {
            'bg': '#f0f0f0',
            'fg': '#000000',
            'activebg': '#e0e0e0',
            'activefg': '#000000'
        }
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)  # Clear button spanning all columns
        ]
        
        for (text, row, column, *span) in buttons:
            button = tk.Button(self.root, text=text, **button_style, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, columnspan=span[0] if span else 1, sticky='nsew')
            button.bind("<Enter>", lambda e, b=button: b.config(bg=button_colors['activebg'], fg=button_colors['activefg']))
            button.bind("<Leave>", lambda e, b=button: b.config(bg=button_colors['bg'], fg=button_colors['fg']))
        
        # Configure rows and columns to expand evenly
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        current_text = self.result_var.get()
        
        if char == 'C':
            self.result_var.set('')
        elif char == '=':
            try:
                expression = current_text.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.result_var.set(result)
            except ZeroDivisionError:
                self.result_var.set('Error: Division by Zero')
            except Exception:
                self.result_var.set('Error')
        else:
            new_text = current_text + char
            self.result_var.set(new_text)
    
    def on_keypress(self, event):
        key = event.char
        if key in '0123456789+-*/.':
            self.on_button_click(key)
        elif key == '\r':  # Enter key
            self.on_button_click('=')
        elif key == '\x08':  # Backspace key
            current_text = self.result_var.get()
            self.result_var.set(current_text[:-1])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()