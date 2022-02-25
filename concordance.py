# %%
from itertools import groupby
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()

# %%
with filedialog.askopenfile(
        title="Choose the file containing token indexes",
        mode="r") as file:
    lines = file.readlines()

# %%
indexed_lines = []
current_index = 0
for line in lines:
    indexed_lines.append((current_index, line))
    current_index += len(line) + 1

# %%


def group_key(entry):
    index, line = entry
    return line.split(maxsplit=1)[0][:3]


grouped = [(k, list(g))
           for k, g in groupby(indexed_lines, key=group_key)]

# %%
with filedialog.asksaveasfile(
        title="Where to save the lazy hashing file",
        mode="w",
        confirmoverwrite=False,
        initialfile="lazyhash.txt") as file:
    for key, occurrences in grouped:
        file.write(f"{key} {occurrences[0][0]}\n")

# %%
