import tkinter as tk
from tkinter import ttk, messagebox

from analysis import load_df, get_tunes_by_book, get_tunes_by_type, search_tunes


class TunesApp:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        master.title("ABC Tunes Browser")
        master.geometry("800x600")

        # Load DataFrame once
        try:
            self.df = load_df()
        except Exception as e:
            messagebox.showerror("DB Error", f"Could not load database: {e}")
            master.destroy()
            return

        # ---------- Top frame: search and filters ----------
        top = ttk.Frame(master)
        top.pack(fill="x", padx=6, pady=6)

        ttk.Label(top, text="Search title:").pack(side="left")
        self.search_var = tk.StringVar()
        ttk.Entry(top, textvariable=self.search_var, width=30).pack(side="left", padx=4)
        ttk.Button(top, text="Search", command=self.do_search).pack(side="left", padx=4)

        ttk.Label(top, text="Book:").pack(side="left", padx=(10, 0))
        self.book_var = tk.StringVar()
        books = sorted(self.df["book"].dropna().unique().tolist())
        combo_books = ["All"] + [str(b) for b in books]
        self.book_cb = ttk.Combobox(top, values=combo_books, width=6, state="readonly")
        self.book_cb.set("All")
        self.book_cb.pack(side="left", padx=4)
        ttk.Button(top, text="Filter", command=self.filter_by_book).pack(
            side="left", padx=4
        )

        ttk.Label(top, text="Type:").pack(side="left", padx=(10, 0))
        types = sorted([r for r in self.df["R"].dropna().unique() if r])
        self.type_cb = ttk.Combobox(top, values=["All"] + types, width=12, state="readonly")
        self.type_cb.set("All")
        self.type_cb.pack(side="left", padx=4)
        ttk.Button(top, text="Filter", command=self.filter_by_type).pack(
            side="left", padx=4
        )

        # ---------- Middle: listbox for tunes ----------
        mid = ttk.Frame(master)
        mid.pack(fill="both", expand=True, padx=6, pady=6)

        self.tune_list = tk.Listbox(mid, width=50)
        self.tune_list.pack(side="left", fill="both", expand=False)
        self.tune_list.bind("<<ListboxSelect>>", self.on_select)

        scrollbar = ttk.Scrollbar(mid, orient="vertical", command=self.tune_list.yview)
        scrollbar.pack(side="left", fill="y")
        self.tune_list.config(yscrollcommand=scrollbar.set)

        # ---------- Right: details text ----------
        self.details = tk.Text(mid)
        self.details.pack(side="left", fill="both", expand=True)

        # load all tunes initially
        self.current_df = self.df.copy()
        self.populate_list(self.current_df)

    # ---------------- Helper methods ----------------

    def populate_list(self, df):
        """Populate the listbox with tunes from the given DataFrame."""
        self.tune_list.delete(0, tk.END)
        self.current_df = df.reset_index(drop=True)
        for _, row in self.current_df.iterrows():
            display = f"{row['X'] or ''} - {row['T'] or '(no title)'}"
            self.tune_list.insert(tk.END, display)
        self.details.delete("1.0", tk.END)

    def do_search(self):
        term = self.search_var.get().strip()
        if not term:
            messagebox.showinfo("Search", "Enter a search term")
            return
        result = search_tunes(self.df, term)
        if result.empty:
            messagebox.showinfo("Search", "No results")
        self.populate_list(result)

    def filter_by_book(self):
        val = self.book_cb.get()
        if val == "All":
            self.populate_list(self.df)
            return
        try:
            b = int(val)
        except ValueError:
            messagebox.showerror("Input", "Book must be a number")
            return
        res = get_tunes_by_book(self.df, b)
        if res.empty:
            messagebox.showinfo("Filter", "No tunes for that book")
        self.populate_list(res)

    def filter_by_type(self):
        val = self.type_cb.get()
        if val == "All" or not val:
            self.populate_list(self.df)
            return
        res = get_tunes_by_type(self.df, val)
        if res.empty:
            messagebox.showinfo("Filter", "No tunes of that type")
        self.populate_list(res)

    def on_select(self, event):
        sel = self.tune_list.curselection()
        if not sel:
            return
        i = sel[0]
        row = self.current_df.iloc[i]
        details = (
            f"Book: {row['book']}\n"
            f"File: {row['filename']}\n"
            f"X: {row['X']}\n"
            f"Title: {row['T']}\n"
            f"Meter: {row['M']}\n"
            f"Key: {row['K']}\n"
            f"Type: {row['R']}\n\n"
            f"Body:\n{row['body']}\n"
        )
        self.details.delete("1.0", tk.END)
        self.details.insert("1.0", details)


if __name__ == "__main__":
    root = tk.Tk()
    app = TunesApp(root)
    root.mainloop()
