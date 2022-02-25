# %%
from tkinter import Tk, filedialog
from typing import TextIO
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


def find_in_corpus(index, word, corpus: TextIO):
    padding = 25
    corpus.seek(index - padding)
    return corpus.read(len(word) + padding * 2).strip().replace("\n", " ")


# %%
with filedialog.askopenfile(title="Corpus text file") as corpus:
    to_print = 10
    int_indexes = [int(i) for i in indexes]
    results = len(int_indexes)
    print("Number of occurrences:", results)
    if results > to_print * 2:
        for index in int_indexes[:to_print]:
            print(find_in_corpus(index, word, corpus))
        print("[...]")
        for index in int_indexes[-to_print:]:
            print(find_in_corpus(index, word, corpus))
    else:
        for index in int_indexes:
            print(find_in_corpus(index, word, corpus))
