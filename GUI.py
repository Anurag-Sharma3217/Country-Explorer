#IMPORT SESSION
import tkinter as tk, function_2 as fun, requests, Storage as st
from tkinter import messagebox

#FUNCTIONs SESSION

def show_country(data):
    name_label.config(text=data.get("name", "Not available"))
    capital_label.config(text=data.get("capital", "Not available"))
    population_label.config(text=data.get("population", 'Not available'))
    for curreny in data.get("currencies", []):
        curreny_code_label.config(text=curreny.get("code", 'Not available'))
        curreny_name_label.config(text=curreny.get("name", 'Not available'))
        curreny_symbol_label.config(text=curreny.get("symbol", 'Not available'))
    for language in data.get("languages", []):
        language_name_label.config(text=language.get("name", 'Not available'))
        language_iso1_label.config(text=language.get("iso639_1", 'Not available'))
        language_iso2_label.config(text=language.get("iso639_2", 'Not available'))
        language_nativename_label.config(text=language.get("nativeName", 'Not available'))

def display_data():
    code = code_entry.get().strip().upper()

    if code is code.isalpha():
        messagebox.showinfo("Input Validation", "Countries's code can only be in letters.")
        return
    
    if len(code) != 2:
        messagebox.showinfo("Input Validation", "Enter a two-letter country code.")

    try:
        data = st.get_saved_country(code)

        if data is None:
            data = fun.fetch_country(code)
            st.save_country(code, data)
            show_country(data)

        else:
            show_country(data)

    except requests.JSONDecodeError as error:
        messagebox.showinfo("JSON Decode Error", {error})

    except requests.ConnectionError:
        messagebox.showinfo("Connection Error", "Could not connect. Check your connection.")
                
    except requests.ConnectTimeout:
        messagebox.showinfo("Timeout", "The request timed out. Try again.")
                
    except requests.HTTPError as error:
        messagebox.showinfo("HTTPError", f"HTTP error: {error}")
                
    except requests.RequestException as error:
        messagebox.showinfo("request Exception", f"Request failed: {error}")                

#WINDOW SESSION
window = tk.Tk()
window.title("Country Explorer")
window.geometry("500x400")

#INPUT FRAME
input_frame = tk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="both")

code_label = tk.Label(input_frame, text="Enter country code:")
code_label.grid()

code_entry = tk.Entry(input_frame)
code_entry.grid()

search_button = tk.Button(input_frame, text="[Search]", command=display_data)
search_button.grid(row=1, column=1)

#OUTCOME FRAME
lable_frame1 = tk.LabelFrame(window, text="[Result Panel]")
lable_frame1.pack(padx=10, pady=10, fill="both", expand=True)

#COUNTRY NAME
label_name = tk.Label(lable_frame1, text="Name:")
label_name.grid(row=0, column=0, sticky="w", padx=5, pady=5)
name_label = tk.Label(lable_frame1, text="")
name_label.grid(row=0, column=1, sticky="w", padx=5, pady=5)

#COUNTRY CAPITAL
label_capital = tk.Label(lable_frame1, text="Capital:")
label_capital.grid(row=1, column=0, sticky="w", padx=5, pady=5)
capital_label = tk.Label(lable_frame1, text="")
capital_label.grid(row=1, column=1, sticky="w", padx=5, pady=5)

#COUNTRY POPULATION
label_population = tk.Label(lable_frame1, text="Population:")
label_population.grid(row=2, column=0, sticky="w", padx=5, pady=5)
population_label = tk.Label(lable_frame1, text="")
population_label.grid(row=2, column=1, sticky="w", padx=5, pady=5)

#COUNTRY CURRENY SESSION
label_code = tk.Label(lable_frame1, text="Curreny code:")
label_code.grid(row=3, column=0, sticky="w", padx=5, pady=5)
curreny_code_label = tk.Label(lable_frame1, text="")
curreny_code_label.grid(row=3, column=1, sticky="w", padx=5, pady=5)

label_name = tk.Label(lable_frame1, text="Curreny name:")
label_name.grid(row=3, column=3, sticky="w", padx=5, pady=5)
curreny_name_label = tk.Label(lable_frame1, text="")
curreny_name_label.grid(row=3,column=4, sticky="w", padx=5, pady=5)

label_symbol = tk.Label(lable_frame1, text="Curreny symbol:")
label_symbol.grid(row=3, column=6, sticky="w", padx=5, pady=5)
curreny_symbol_label = tk.Label(lable_frame1, text="")
curreny_symbol_label.grid(row=3, column=7, sticky="w", padx=5, pady=5)

#COUNTRY LANGUAGE SESSION
label_language_name = tk.Label(lable_frame1, text="Name:")
label_language_name.grid(row=4, column=0, sticky="w", padx=5, pady=5)
language_name_label = tk.Label(lable_frame1, text="")
language_name_label.grid(row=4, column=1, sticky="w", padx=5, pady=5)

label_language_iso639_1 = tk.Label(lable_frame1, text="iso639_1:")
label_language_iso639_1.grid(row=4, column=3, sticky="w", padx=5, pady=5)
language_iso1_label = tk.Label(lable_frame1, text="")
language_iso1_label.grid(row=4, column=4, sticky="w", padx=5, pady=5)

label_language_iso639_2 = tk.Label(lable_frame1, text="iso639_2:")
label_language_iso639_2.grid(row=4, column=6, sticky="w", padx=5, pady=5)
language_iso2_label = tk.Label(lable_frame1, text="")
language_iso2_label.grid(row=4, column=7, sticky="w", padx=5, pady=5)

label_language_nativename = tk.Label(lable_frame1, text="Nativename:")
label_language_nativename.grid(row=4, column=9, sticky="w", padx=5, pady=5)
language_nativename_label = tk.Label(lable_frame1, text="")
language_nativename_label.grid(row=4, column=10, sticky="w", padx=5, pady=5)

window.mainloop()