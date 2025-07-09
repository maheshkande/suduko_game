import tkinter as tk

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Sudoku Game")
        self.entries = []

        self.create_grid()

    def create_grid(self):
        for row in range(9):
            row_entries = []
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 20), justify='center', borderwidth=2, relief='ridge')
                entry.grid(row=row, column=col, padx=2, pady=2)

                # Thicker border for 3x3 boxes
                if col % 3 == 0:
                    entry.grid_configure(padx=(4, 2))
                if row % 3 == 0:
                    entry.grid_configure(pady=(4, 2))

                row_entries.append(entry)
            self.entries.append(row_entries)

    def get_grid_values(self):
        grid = []
        for row in self.entries:
            row_vals = []
            for entry in row:
                val = entry.get()
                row_vals.append(int(val) if val.isdigit() else 0)
            grid.append(row_vals)
        return grid

# --- Main app ---
if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
