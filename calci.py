import tkinter as tk
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = "#fffbf7"
class calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("375x467")
        self.window.resizable(0, 0)
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = ""
        self.current_expression = ""
        self.total_label, self.lable = self.create_display_label()
        self.digits = { 
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)}
        self.create_digit_button()
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_operator_button()
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_root_button()
        self.bind_keys()
        self.buttons_frame.grid_rowconfigure(0, weight=1)

        for x in range(1,5):
            self.buttons_frame.grid_rowconfigure(x, weight=1)
            self.buttons_frame.grid_columnconfigure(x, weight=1)

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#f5f5f5",fg="#25265e", padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        lable = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#f5f5f5",fg="#25265e", padx=24, font=LARGE_FONT_STYLE)
        lable.pack(expand=True, fill="both")

        return total_label, lable
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_lable()
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_lable()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_lable()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg="#f5f5f5")
        frame.pack(expand=True, fill="both")
        return frame
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_button(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text = str(digit), bg="#ffffff", fg= '#25265e', font=DIGIT_FONT_STYLE,borderwidth=0,highlightbackground="red", command= lambda x = digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
    def create_operator_button(self):
        i = 0
        for operators,symbols in self.operations.items():
            buton = tk.Button(self.buttons_frame, text=symbols, bg=OFF_WHITE, fg="#25265e", font=DEFAULT_FONT_STYLE, borderwidth=0, command= lambda x = operators: self.append_operator(x))
            buton.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1
    def create_clear_button(self):
        buton = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg="#25265e", font=DEFAULT_FONT_STYLE, borderwidth=0, command= self.clear)
        buton.grid(row=0, column=1, columnspan=1,sticky=tk.NSEW)
    
    def square(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(f"{self.total_expression}**2"))
        self.total_expression = ""
        self.update_lable()

    def root(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(f"{self.total_expression}**0.5"))
        self.total_expression = ""
        self.update_lable()

    def create_square_button(self):
        buton = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg="#25265e", font=DEFAULT_FONT_STYLE, borderwidth=0, command= self.square)
        buton.grid(row=0, column=2, columnspan=1,sticky=tk.NSEW)  
    def create_root_button(self):
        buton = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg="#25265e", font=DEFAULT_FONT_STYLE, borderwidth=0, command= self.root)
        buton.grid(row=0, column=3, columnspan=1,sticky=tk.NSEW)
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Math Error"
        finally:
            self.update_lable()

    def create_equal_button(self):
        buton = tk.Button(self.buttons_frame, text="=", bg="#ffd25c", fg="#25265e", font=DEFAULT_FONT_STYLE, borderwidth=0, command= self.evaluate)
        buton.grid(row=4, column=3, columnspan=2,sticky=tk.NSEW)

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_lable(self):
        self.lable.config(text=self.current_expression[:11])

    
    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    calculator = calculator()
    calculator.run()