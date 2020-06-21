# Broccoli

🥦 Broccoli is the quick and dirty [Skribbl.io](https://skribbl.io) game cheater that tries to guess what word the host is drawing based on the given information. It is a simple, inefficient Python script with a command line interface.

## Getting Started

To get started, clone or download the repository. You'll need the files `query.py` and `wordlist.txt`. Run

```bash
python query.py
```

and you'll be greeted with a command-line interface.

```bash
==[ skribblio cheater by gid ]==

enter query >
```

Here, you can enter the query of your choice. Special keywords execute certain actions. By typing `sort`, the list is resorted, which will help the program print solutions faster (it is reccomended you use PyPy over CPython, but with small wordlists, runtime makes no difference as it a difference of milliseconds). The command `add` allows you to add a new word to the dictionary if it wasn't there before, and `exit` will allow you to exit the program.

Additional commands include `clear` which will clear the screen, and `quit` which does the same thing as `exit`.

## Usage

To use the program, simply either type a number like `6` to see all words that are 6 letters long, or type letters with wildcards, like `???a` to see words where the fourth letter is `a`. This is useful after a letter has been revealed, or if there is a space in the word, you can type `???? ????` to account for the space.

## Contribution

If you'd like to contribute additional wordlists or improve the codebase, simply submit a pull request. I am looking to build a Chrome extension to allow this to run while the game is running!
