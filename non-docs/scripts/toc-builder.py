import os

# Path to the wiki directory
wiki_dir = '/home/daniel/Git/wiki'
toc_path = os.path.join(wiki_dir, 'toc.md')

# Ensure the directory exists
os.makedirs(wiki_dir, exist_ok=True)

def capitalize_title(title):
    """Capitalize the first letter of a title."""
    return title.capitalize()

def generate_toc(directory):
    """Generate a Table of Contents for the given directory."""
    toc_lines = ['# Table of Contents\n']
    for root, dirs, files in os.walk(directory):
        # Exclude dot directories (e.g., .git, .vscode) and 'non-docs' folder
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'non-docs']
        
        # Calculate indentation level based on folder depth
        level = root.replace(directory, '').count(os.sep)
        indent = '  ' * level
        
        # Add directories to TOC
        if root != directory:
            folder_name = capitalize_title(os.path.basename(root))
            toc_lines.append(f"{indent}- **{folder_name}/**")
        
        # Add Markdown files to TOC, excluding images
        for file in sorted(files):
            if file.endswith('.md') and file != 'README.md':  # Exclude README.md itself
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                toc_lines.append(f"{indent}  - [{file}]({relative_path})")
    
    return '\n'.join(toc_lines)

# Generate TOC and write it to toc.md
toc_content = generate_toc(wiki_dir)
with open(toc_path, 'w') as toc_file:
    toc_file.write(toc_content)

print(f"Table of Contents updated and written to {toc_path}")