# 🧠 Brotherhood Calculator – GUI & CLI Edition

> **Note:** Will implement this with more accuracy as actual with trained models in the future.

A modern Python application to calculate the "Brotherhood Percentage" between two names, featuring both a beautiful GUI (with tkinter) and a convenient CLI mode for headless environments like GitHub Codespaces.

---

## 🚀 Features
- **GUI Mode:**
  - Sleek, user-friendly interface using `tkinter` and `ttk` widgets
  - Enter two names, click **Calculate**, and see the brotherhood percentage and relationship label with emoji and color feedback
  - **Clear** button to reset inputs and results
  - Input validation and helpful tooltips
- **CLI Mode:**
  - Run in any terminal (perfect for Codespaces or servers)
  - Interactive prompts for names, instant results, and relationship labels
  - Auto-fallback to CLI if GUI cannot start
- **Smart Similarity:**
  - Uses `difflib.SequenceMatcher` for string similarity
  - Relationship labels: Soul Brothers 🫂, Close Comrades 🤝, Good Acquaintances, Just Names 😅
- **Ready for the Future:**
  - Plans to use trained models for even more accurate results

---

## 🖥️ How to Run

### 1. GUI Mode (Desktop Environments)
```bash
python Brotherhood01.py
```
- A window will open. Enter two names, click **Calculate**, and view the results!

### 2. CLI Mode (Codespaces, Servers, or Terminal Lovers)
```bash
python Brotherhood01.py --cli
```
- Follow the prompts in your terminal. Type `q` to quit at any time.

> **Tip:** If you run without `--cli` and the GUI cannot start, the program will automatically switch to CLI mode.

---

## 📝 Example (CLI)
```
🧠 Brotherhood Calculator (CLI Mode)
Enter two names to calculate how similar they are. The closer the percentage, the stronger the 'brotherhood'!

Name 1 (or 'q' to quit): tuntun
Name 2 (or 'q' to quit): natunatu
Brotherhood Percentage: 71.43%
Relationship: Close Comrades 🤝
```

---

## 📦 Requirements
- Python 3.x
- `tkinter` (for GUI, usually included with Python)
- `difflib` (Python standard library)

---

## 🛠️ Project Structure
```
Brotherhood01.py   # Main application (GUI + CLI)
README.md          # This file
LICENSE            # MIT License
```

---

## 🤝 Contributing
Pull requests, feature suggestions, and issues are welcome! Feel free to fork and improve.

---

## 📄 License
MIT License – see [LICENSE](LICENSE) for details.

