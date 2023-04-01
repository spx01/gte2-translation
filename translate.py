import deepl
import re
import os

source_path = "ftbquests"
target_path = "ftbquests-tl"

auth_key = os.environ["DEEPL_AUTH_KEY"]
tl = deepl.Translator(auth_key)

# this matches every "" sequence that contains a non-ascii unicode character
# also accounts for escaped \" groups inside the double quotes
match_jap = r'"((?:\\.|[^\\"\n\r])*)[\u0080-\uffff]((?:\\.|[^\\"\n\r])*)"'


# replace matches of the r regex in s with f(match)
def regex_replace(r, s, f):
    new = ""
    start = 0
    for m in re.finditer(r, s):
        end, newstart = m.span()
        new += s[start:end]
        new += f(m.group())
        start = newstart
    new += s[start:]
    return new


def copy_structure(src, dst):
    for dirpath, dirnames, _ in os.walk(src):
        for d in dirnames:
            os.makedirs(
                os.path.join(dst, *dirpath.split(os.path.sep)[1:], d),
                exist_ok=True,
            )


def translate(s):
    # un-escape the string so that it doesnt confuse deepl
    res = s[1:-1].replace('\\"', '"')
    res = tl.translate_text(
        res, source_lang="JA", target_lang="EN-US", preserve_formatting=True
    ).text
    return '"' + res.replace('"', '\\"') + '"'


def create_file_set(path, f=lambda s: s.endswith(".snbt")):
    res = set()
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if not f(filename):
                continue
            file = os.path.join(dirpath, filename)
            if os.path.isfile(file):
                res.add(os.path.join(*file.split(os.path.sep)[1:]))
    return res


def main():
    copy_structure(source_path, target_path)
    ofiles = create_file_set(source_path)
    tlfiles = create_file_set(target_path)
    to_translate = ofiles - tlfiles
    for fp in to_translate:
        with open(os.path.join(source_path, fp), "r") as f:
            s = f.read()
            print(f"translating {fp}...")
            translated = regex_replace(match_jap, s, translate)
            with open(os.path.join(target_path, fp), "x") as tf:
                tf.write(translated)


main()
