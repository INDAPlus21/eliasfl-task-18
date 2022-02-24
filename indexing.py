# %%
from itertools import groupby
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()

print("Enter token file")
with filedialog.askopenfile(title="Tokens file") as tokens:
    words = tokens.readlines()


# %%
print("Splitting words")
obj_words = (word.strip().split() for word in words)


# %%
print("Grouping by token")
grouped = (list(g) for k, g in groupby(obj_words, key=lambda x: x[0]))


# %%
print("Combining group to single line")
combined = (
    f"{items[0][0]} {' '.join(b for a, b in items)}" for items in grouped)


# %%
print("Enter file where to save new token index")
with filedialog.asksaveasfile(
        title="Final index file",
        initialfile="index.txt",
        confirmoverwrite=False,
        mode="w") as index:
    index.writelines(f"{line}\n" for line in combined)
print("Done!")
