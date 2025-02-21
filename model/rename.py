import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

jpg_files = sorted([f for f in os.listdir() if f.endswith(".jpg")])
txt_files = sorted([f for f in os.listdir() if f.endswith(".txt")])

for i, file in enumerate(jpg_files, start=1):
    new_name = f"{i+33}.jpg"
    os.rename(file, new_name)
    print(f"Renamed {file} -> {new_name}")

for i, file in enumerate(txt_files, start=1):
    new_name = f"{i}.txt"
    os.rename(file, new_name)
    print(f"Renamed {file} -> {new_name}")

print("Renaming completed.")
