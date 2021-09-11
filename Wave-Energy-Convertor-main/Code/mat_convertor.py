import tkinter as tk
from tkinter import filedialog
import scipy.io


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
mat = scipy.io.loadmat(file_path)

SA = mat['SA'].item()
