def write_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)
    print(f"File '{filename}' created with text.")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("File contents:", f.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def append_file(filename, text):
    with open(filename, "a") as f:
        f.write("\n" + text)
    print(f"Text appended to '{filename}'.")

def delete_file(filename):
    import os
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' not found.")
