import sys
import tkinter as tk
from tkinter import ttk, messagebox
from difflib import SequenceMatcher

# --- Calculation logic (shared by GUI and CLI) ---
def calculate_brotherhood(name1: str, name2: str):
    """Calculate brotherhood percentage and relationship label."""
    name1 = name1.strip().lower()
    name2 = name2.strip().lower()
    if not name1 or not name2:
        return None, None, None
    ratio = SequenceMatcher(None, name1, name2).ratio()
    percent = round(ratio * 100, 2)
    if percent >= 90:
        relation = "Soul Brothers 🫂"
        color = "#1e90ff"
    elif percent >= 70:
        relation = "Close Comrades 🤝"
        color = "#28a745"
    elif percent >= 50:
        relation = "Good Acquaintances"
        color = "#ffc107"
    else:
        relation = "Just Names 😅"
        color = "#dc3545"
    return percent, relation, color

# --- GUI Application ---
class BrotherhoodCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Brotherhood Calculator")
        self.root.resizable(False, False)
        self.root.geometry("400x300")
        self.root.configure(padx=20, pady=20)

        # Tooltip/description
        desc = ttk.Label(root, text="Enter two names to calculate how similar they are. The closer the percentage, the stronger the 'brotherhood'!", wraplength=360, foreground="#555")
        desc.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # Name 1
        ttk.Label(root, text="Name 1:").grid(row=1, column=0, sticky="e", padx=(0, 5), pady=5)
        self.name1_var = tk.StringVar()
        self.name1_entry = ttk.Entry(root, textvariable=self.name1_var, width=25)
        self.name1_entry.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)

        # Name 2
        ttk.Label(root, text="Name 2:").grid(row=2, column=0, sticky="e", padx=(0, 5), pady=5)
        self.name2_var = tk.StringVar()
        self.name2_entry = ttk.Entry(root, textvariable=self.name2_var, width=25)
        self.name2_entry.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)

        # Buttons
        self.calc_btn = ttk.Button(root, text="Calculate", command=self.calculate)
        self.calc_btn.grid(row=3, column=1, sticky="e", padx=5, pady=15)
        self.clear_btn = ttk.Button(root, text="Clear", command=self.clear)
        self.clear_btn.grid(row=3, column=2, sticky="w", padx=5, pady=15)

        # Result label
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(root, textvariable=self.result_var, font=("Arial", 12, "bold"))
        self.result_label.grid(row=4, column=0, columnspan=3, pady=(10, 2))

        # Relationship label
        self.relation_var = tk.StringVar()
        self.relation_label = ttk.Label(root, textvariable=self.relation_var, font=("Arial", 11))
        self.relation_label.grid(row=5, column=0, columnspan=3, pady=(0, 5))

    def calculate(self):
        name1 = self.name1_var.get()
        name2 = self.name2_var.get()
        percent, relation, color = calculate_brotherhood(name1, name2)
        if percent is None:
            messagebox.showwarning("Input Error", "Both name fields must be filled.")
            return
        self.result_var.set(f"Brotherhood Percentage: {percent}%")
        self.relation_var.set(f"Relationship: {relation}")
        self.result_label.configure(foreground=color)
        self.relation_label.configure(foreground=color)

    def clear(self):
        self.name1_var.set("")
        self.name2_var.set("")
        self.result_var.set("")
        self.relation_var.set("")
        self.result_label.configure(foreground="#000")
        self.relation_label.configure(foreground="#000")

# --- CLI Application ---
def run_cli():
    print("🧠 Brotherhood Calculator (CLI Mode)")
    print("Enter two names to calculate how similar they are. The closer the percentage, the stronger the 'brotherhood'!\n")
    while True:
        name1 = input("Name 1 (or 'q' to quit): ").strip()
        if name1.lower() == 'q':
            break
        name2 = input("Name 2 (or 'q' to quit): ").strip()
        if name2.lower() == 'q':
            break
        percent, relation, _ = calculate_brotherhood(name1, name2)
        if percent is None:
            print("Both name fields must be filled.\n")
            continue
        print(f"Brotherhood Percentage: {percent}%")
        print(f"Relationship: {relation}\n")

if __name__ == "__main__":
    force_cli = '--cli' in sys.argv
    if force_cli:
        run_cli()
    else:
        try:
            root = tk.Tk()
            app = BrotherhoodCalculator(root)
            root.mainloop()
        except Exception as e:
            print("GUI could not be started (likely due to no display). Falling back to CLI mode.")
            print(f"Reason: {e}\n")
            run_cli()
