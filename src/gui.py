import tkinter as tk
import controller as ctrl

def run_app(model, mean, std, device):
    root = tk.Tk()
    root.title("Passenger Survival Predictor")
    root.geometry("500x500")

    title = tk.Label(root, text="Passenger Survival Predictor", font=("Arial", 16, "bold"))
    title.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="Sex: ").grid(row=0, column=0)
    sex_label = tk.Label(frame, text="")
    sex_label.grid(row=0, column=1)

    tk.Label(frame, text="Age: ").grid(row=1, column=0)
    age_label = tk.Label(frame, text="")
    age_label.grid(row=1, column=1)

    tk.Label(frame, text="Age_missing: ").grid(row=2, column=0)
    age_missing_label = tk.Label(frame, text="")
    age_missing_label.grid(row=2, column=1)

    tk.Label(frame, text="Class: ").grid(row=3, column=0)
    class_label = tk.Label(frame, text="")
    class_label.grid(row=3, column=1)

    tk.Label(frame, text="Crew: ").grid(row=4, column=0)
    crew_label = tk.Label(frame, text="")
    crew_label.grid(row=4, column=1)

    tk.Label(frame, text="Ground Truth: ").grid(row=5, column=0)
    gt_label = tk.Label(frame, text="")
    gt_label.grid(row=5, column=1)

    result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
    result_label.pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=15)

    tk.Button(
        button_frame,
        text="Predici",
        command=lambda: ctrl.handle_predict(
            model, mean, std, device, 
            sex_label, age_label, age_missing_label, 
            class_label, crew_label, result_label
        ),
        width=12
    ).grid(row=1, column=0, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="Reset",
        command=lambda: ctrl.reset(
            sex_label, age_label, age_missing_label, 
            class_label, crew_label, gt_label, result_label
        ),
        width=12
    ).grid(row=1, column=1, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="Carica CSV",
        command=ctrl.load_csv,
        width=12
    ).grid(row=0, column=0, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="Esempio Casuale",
        command=lambda: ctrl.load_random_row(
            sex_label, age_label, age_missing_label,
            class_label, crew_label, gt_label
        ),
        width=12
    ).grid(row=0, column=1, padx=10, pady=10)

    root.mainloop()