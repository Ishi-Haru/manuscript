def select_npy_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="npyファイルを選択してください",
        filetypes=[("NumPy files", "*.npy")],
        initialdir="."
    )
