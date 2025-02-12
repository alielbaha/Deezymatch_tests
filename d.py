from graphviz import Digraph

def tree_(input_string, replacement_dict, deleted_chars):
    tree = Digraph("Rectree")
    tree.node("root", "")

    def dfs(index, current, parent_id, restored_chars):
       
        if index == len(input_string):
            full_string = list(current)
            for pos, char in sorted(deleted_chars):
                if pos < len(full_string):
                    full_string.insert(pos, char)
                else:
                    full_string.append(char) 
            restored_version = "".join(full_string)

            leaf_id = f"leaf_{restored_version}"
            tree.node(leaf_id, restored_version, shape="box")
            tree.edge(parent_id, leaf_id)
            return

        for length in range(1, len(input_string) - index + 1):
            substring = input_string[index:index + length]
          
            if substring in replacement_dict:
                for replacement in replacement_dict[substring]:
                    child_id = f"{current + replacement}_{index + length}"
                    tree.node(child_id, current + replacement)
                    tree.edge(parent_id, child_id)
                    dfs(index + length, current + replacement, child_id, restored_chars)

            child_id = f"{current + substring}_{index + length}"
            tree.node(child_id, current + substring)
            tree.edge(parent_id, child_id)
            dfs(index + length, current + substring, child_id, restored_chars)

    dfs(0, "", "root", deleted_chars)
    return tree


newr = []
prev_char = None
for i, c in enumerate(r):
    if c != prev_char:
        newr.append(c)
    else:
        deleted_chars.append((i, c))  # Track duplicate removal
    prev_char = c
r = "".join(newr)

for match in re.finditer(r'([^PCS])H', r):
    pos = match.start() + 1
    deleted_chars.append((pos, 'H'))
r = re.sub(r'([^PCS])H', r'\1', r)



for match in re.finditer(r'[TX]$', r):
    pos = match.start()
    deleted_chars.append((pos, r[pos]))
r = re.sub(r'(.*)[TX]$', r'\1', r) 
