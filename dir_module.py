import os

def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)
        print(f"Directory '{name}' created.")
    else:
        print(f"Directory '{name}' already exists.")

def list_dir(path="."):
    print("Contents:", os.listdir(path))

def rename_dir(old, new):
    if os.path.exists(old):
        os.rename(old, new)
        print(f"Directory renamed from '{old}' to '{new}'.")
    else:
        print(f"Directory '{old}' not found.")

def remove_dir(name):
    if os.path.exists(name):
        os.rmdir(name)
        print(f"Directory '{name}' removed.")
    else:
        print(f"Directory '{name}' not found.")
