#!/usr/bin/env python3
import os
import random

# ← EDIT THESE
PARENT_FOLDER = "/Users/cynthia/Downloads/AI"
KEEP_PER_SUBFOLDER = 312

def prune_folder(folder: str, keep: int):
    files = [f for f in os.listdir(folder)
             if os.path.isfile(os.path.join(folder, f))]
    total = len(files)
    if keep < 0:
        print(f"❌ {folder}: “keep” must be ≥ 0.")
        return
    if keep >= total:
        print(f"⚠️  {folder}: {total} files found; nothing to delete.")
        return

    to_delete = random.sample(files, total - keep)
    for fname in to_delete:
        try:
            os.remove(os.path.join(folder, fname))
            print(f"Deleted from {os.path.basename(folder)}: {fname}")
        except Exception as e:
            print(f"Error deleting {fname} in {folder}: {e}")

    print(f"✅ {folder}: kept {keep}, deleted {len(to_delete)}.")

def main():
    if not os.path.isdir(PARENT_FOLDER):
        print(f"❌ '{PARENT_FOLDER}' is not a directory.")
        return

    for entry in os.listdir(PARENT_FOLDER):
        sub = os.path.join(PARENT_FOLDER, entry)
        if os.path.isdir(sub):
            prune_folder(sub, KEEP_PER_SUBFOLDER)

if __name__ == "__main__":
    main()
