import tkinter as tk
from tkinter import ttk, messagebox

# =====================
# Données
# =====================
suspects = ["john", "mary", "alice", "bruno", "sophie"]
crimes = ["vol", "assassinat", "escroquerie"]

has_motive = {
    ("john", "vol"),
    ("mary", "assassinat"),
    ("alice", "escroquerie")
}

was_near_crime_scene = {
    ("john", "vol"),
    ("mary", "assassinat")
}

has_fingerprint_on_weapon = {
    ("john", "vol"),
    ("mary", "assassinat")
}

has_bank_transaction = {
    ("alice", "escroquerie"),
    ("bruno", "escroquerie")
}

owns_fake_identity = {
    ("sophie", "escroquerie")
}

# =====================
# Règles is_guilty)
# =====================
def is_guilty(suspect, crime):
    if crime == "vol":
        return (
            (suspect, "vol") in has_motive and
            (suspect, "vol") in was_near_crime_scene and
            (suspect, "vol") in has_fingerprint_on_weapon
        )

    elif crime == "assassinat":
        return (
            (suspect, "assassinat") in has_motive and
            (suspect, "assassinat") in was_near_crime_scene and
            (
                (suspect, "assassinat") in has_fingerprint_on_weapon
            )
        )

    elif crime == "escroquerie":
        return (
            ((suspect, "escroquerie") in has_motive and
             (suspect, "escroquerie") in has_bank_transaction)
            or (suspect, "escroquerie") in owns_fake_identity
        )

    return False

# =====================
# Interface Tkinter
# =====================
def check_verdict():
    suspect = suspect_var.get()
    crime = crime_var.get()

    if not suspect or not crime:
        messagebox.showwarning("Erreur", "Choisis un suspect et un crime.")
        return

    guilty = is_guilty(suspect, crime)
    if guilty:
        messagebox.showinfo("Verdict", f"{suspect.capitalize()} est COUPABLE pour {crime}.")
    else:
        messagebox.showinfo("Verdict", f"{suspect.capitalize()} est NON COUPABLE pour {crime}.")

# Fenêtre principale
root = tk.Tk()
root.title("Système Expert - Crimes")
root.geometry("400x250")

# Labels
tk.Label(root, text="Choisis un suspect :", font=("Arial", 12)).pack(pady=5)
suspect_var = tk.StringVar()
suspect_menu = ttk.Combobox(root, textvariable=suspect_var, values=suspects, state="readonly")
suspect_menu.pack()

tk.Label(root, text="Choisis un crime :", font=("Arial", 12)).pack(pady=5)
crime_var = tk.StringVar()
crime_menu = ttk.Combobox(root, textvariable=crime_var, values=crimes, state="readonly")
crime_menu.pack()

# Bouton
tk.Button(root, text="Vérifier", command=check_verdict, font=("Arial", 12), bg="lightblue").pack(pady=20)

# Lancer l'app
root.mainloop()
