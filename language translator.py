import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from playsound import playsound
import os

# Initialize translator
translator = Translator()

# Build a simple GUI
root = tk.Tk()
root.title("Translator with TTS")

tk.Label(root, text="Text to translate:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_text = tk.Text(root, height=5, width=40)
input_text.grid(row=1, column=0, columnspan=2, padx=5)

tk.Label(root, text="From:").grid(row=2, column=0, sticky="e")
tk.Label(root, text="To:").grid(row=2, column=1, sticky="e")

# Prepare language selection
lang_codes = list(LANGUAGES.keys())
lang_names = [LANGUAGES[code].title() for code in lang_codes]
src_var = tk.StringVar(value="English")
dst_var = tk.StringVar(value="French")
src_menu = ttk.Combobox(root, textvariable=src_var, values=lang_names, state="readonly")
dst_menu = ttk.Combobox(root, textvariable=dst_var, values=lang_names, state="readonly")
src_menu.grid(row=3, column=0, padx=5, sticky="ew")
dst_menu.grid(row=3, column=1, padx=5, sticky="ew")

tk.Label(root, text="Translation:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
output_text = tk.Text(root, height=5, width=40)
output_text.grid(row=5, column=0, columnspan=2, padx=5)

def translate():
    src_lang_name = src_var.get().lower()
    dst_lang_name = dst_var.get().lower()
    # Find the corresponding language codes
    lang_map = {name.lower(): code for code, name in LANGUAGES.items()}
    src_code = lang_map.get(src_lang_name, 'auto')
    dst_code = lang_map.get(dst_lang_name, 'en')
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input needed", "Please enter text to translate.")
        return
    try:
        result = translator.translate(text, src=src_code, dest=dst_code)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def speak_text():
    # Get the translated text
    text = output_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("No text", "Please translate text first.")
        return
    # Determine target language code
    dst_lang_name = dst_var.get().lower()
    lang_map = {name.lower(): code for code, name in LANGUAGES.items()}
    dst_code = lang_map.get(dst_lang_name, 'en')
    # Use gTTS to generate speech
    try:
        tts = gTTS(text=text, lang=dst_code)
        tts.save("temp_speech.mp3")
        playsound("temp_speech.mp3")
        os.remove("temp_speech.mp3")
    except Exception as e:
        messagebox.showerror("TTS Error", str(e))

# Buttons
tk.Button(root, text="Translate", command=translate).grid(row=6, column=0, pady=10)
tk.Button(root, text="Speak", command=speak_text).grid(row=6, column=1, pady=10)

root.mainloop()
