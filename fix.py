import os, pathlib, re

# 1. Images rename
path = "home/static/images"
if os.path.exists(path):
    for f in os.listdir(path):
        new = f.lower().replace(" ", "-")
        if f != new:
            os.rename(os.path.join(path, f), os.path.join(path, new))
            print(f"{f} -> {new}")

# 2. HTML fix
for file in pathlib.Path("home").rglob("*.html"):
    txt = file.read_text(encoding="utf-8")
    new_txt = txt.replace("{% static-'", "{% static '").replace("{% static -'", "{% static '")
    new_txt = re.sub(r"images/([^'\"\)]+)", lambda m: "images/" + m.group(1).lower().replace(" ", "-"), new_txt)
    if txt != new_txt:
        file.write_text(new_txt, encoding="utf-8")
        print(f"Fixed {file}")

print("Ho gaya! Ab bas upload karna hai.")