import torch
import pandas as pd
from tkinter import messagebox, filedialog
import random

from model import predict

df_loaded = None
current_index = None

def load_csv():
    global df_loaded, current_index

    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return
    
    try:
        df_loaded = pd.read_csv(file_path)
        current_index = None
        messagebox.showinfo("Caricamento CSV", f"Dataset caricato: {len(df_loaded)} esempi.")
    except Exception as e:
        messagebox.showerror("Errore", f"Impossibile caricare il CSV:\n {e}")

def load_random_row(sex_label, age_label, age_missing_label, class_label, crew_label, gt_label):
    global df_loaded, current_index

    if df_loaded is None or len(df_loaded) == 0:
        messagebox.showwarning("Attenzione", "Nessun dataset caricato.")
        return
    
    current_index = random.randint(0, len(df_loaded) - 1)
    row = df_loaded.iloc[current_index]

    sex_label.config(text=str(row.get("sex")))
    age_label.config(text=str(row.get("age")))
    age_missing_label.config(text=str(row.get("age_missing")))
    class_label.config(text=str(row.get("class")))
    crew_label.config(text=str(row.get("crew")))

    gt_label.config(text=str(row.get("survived")))

def handle_predict(model, mean, std, device, sex_label, age_label, age_missing_label, class_label, crew_label, result_label):
    try:
        sex = float(sex_label.cget("text"))
        age = float(age_label.cget("text"))
        age_missing = float(age_missing_label.cget("text"))
        pclass = float(class_label.cget("text"))
        crew = float(crew_label.cget("text"))

        features = [sex, age, age_missing, pclass, crew]

        pred, prob = predict(model, mean, std, device, features)

        if pred == 1:
            result_label.config(text=f"SOPRAVVISSUTO\nProbabilità: {prob * 100:.2f}%", fg="green")
        else:
            result_label.config(text=f"NON SOPRAVVISSUTO\nProbabilità: {(1 - prob) * 100:.2f}%", fg="red")

    except Exception as e:
        messagebox.showerror("Errore", f"Errore nella predizione.\n{e}")

def reset(sex_label, age_label, age_missing_label, class_label, crew_label, gt_label, result_label):
    global df_loaded, current_index

    df_loaded = None
    current_index = None

    sex_label.config(text="")
    age_label.config(text="")
    age_missing_label.config(text="")
    class_label.config(text="")
    crew_label.config(text="")
    gt_label.config(text="")
    result_label.config(text="")
