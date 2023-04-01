import filecmp
import os

old_dir = "ftbquests"
update_dir = "ftbquests-new"
tl_dir = "ftbquests-tl"


def find_new_files(d, l=[]):
    for name in d.diff_files:
        l.append(os.path.join(d.right, name))
    for sub in d.subdirs.values():
        find_new_files(sub, l)
    return l


def main():
    cmp = filecmp.dircmp(old_dir, update_dir)
    new_files = find_new_files(cmp)

    for p in new_files:
        tl_path = os.path.join(tl_dir, *p.split(os.path.sep)[1:])
        if os.path.isfile(tl_path):
            print(f"removing {tl_path}...")
            os.remove(tl_path)


main()
