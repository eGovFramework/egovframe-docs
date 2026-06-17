import re
import os

with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

tree_blocks = re.findall(r"```(.*?)```", readme_content, re.DOTALL)
tree_text = tree_blocks[0] # the first one contains the dir tree

current_dir = ""
expected_files = []

lines = tree_text.strip().split("\n")
dir_stack = {} 

def get_level(line):
    match = re.match(r"^[│ ├└─]*", line)
    return len(match.group(0))

for line in lines:
    if not line.strip(): continue
    
    match = re.search(r"(/[\w.-]+)", line)
    if match:
        name = match.group(1).lstrip("/")
        level = get_level(line)
        
        if name.endswith(".md"):
            parent_dir = ""
            if level > 0:
                parent_keys = [k for k in sorted(dir_stack.keys()) if k < level]
                if parent_keys:
                    parent_dir = "/".join([dir_stack[k] for k in parent_keys]) + "/"
            
            full_path = parent_dir + name
            expected_files.append(full_path)
        else:
            dir_stack[level] = name
            keys_to_remove = [k for k in dir_stack.keys() if k > level]
            for k in keys_to_remove:
                del dir_stack[k]

missing_files = []
for f in expected_files:
    if not os.path.exists(f):
        missing_files.append(f)

print(f"Total expected files from README: {len(expected_files)}")
print("Missing files:")
for mf in missing_files:
    print(f" - {mf}")
