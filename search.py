# %%
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()

# %%
with filedialog.askopenfile(title="Open lazyhash magicfile") as file:
    # read lines from bottom to get longest hash match
    lines = [tuple(line.split(maxsplit=1))
             for line in reversed(file.readlines())]
lines = [(a, int(b.strip())) for (a, b) in lines]

# %%
query = input("Word to search for: ").strip().lower()
try:
    (target_key, target_index) = next((key, index)
                                      for key, index in lines if query[:3] == key)
except StopIteration:
    print("Word not found in hash file")

# %%
word_indexes = []
with filedialog.askopenfile(title="Open word index file") as file:
    file.seek(target_index)
    [word, *indexes] = file.readline().strip().split()
    while word != query and word.startswith(target_key) and file.readable():
        [word, *indexes] = file.readline().strip().split()
    if word != query:
        print("Word not found in index file")

# %%
indexes = [int(i) for i in indexes]
print(word, indexes)

# %%
to_print = 10
if len(indexes) > to_print:
    for index in indexes[:to_print]:
        pass
    print("[...]")
    for index in indexes[-to_print:]:
        pass
