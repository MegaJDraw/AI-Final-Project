import os

def should_ignore(name):
    ignore_list = [
        "__pycache__",
        "__init__.py",
        ".git",
        ".gitignore",
        ".gitattributes",
    ]
    return name in ignore_list or name.startswith(".")

def convert_directory_to_markdown(directory, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(directory):
            # Ignore specified directories
            dirs[:] = [d for d in dirs if not should_ignore(d)]

            # Write the directory path as a heading
            relative_path = os.path.relpath(root, directory)
            if relative_path != ".":
                f.write(f"# {relative_path}\n\n")

            # Write each file in the directory
            for file in files:
                if should_ignore(file):
                    continue

                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as file_content:
                        content = file_content.read()
                        f.write(f"## {file}\n\n")
                        f.write(content)
                        f.write("\n\n")
                except UnicodeDecodeError:
                    print(f"Skipping file: {file_path} (cannot decode using UTF-8)")
                    continue

# Get the current directory
current_directory = os.getcwd()

# Output file name
output_file = "repository.md"

# Convert all files in the current directory and its subdirectories to a single Markdown file
convert_directory_to_markdown(current_directory, output_file)