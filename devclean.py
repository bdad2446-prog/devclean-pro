import os
import shutil

categories = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.html': 'Html',
    '.css': 'Css',
    '.jpeg': 'Images',
    '.jpg': 'Images',
    '.png': 'Images',
    '.kt': 'Kotlin',
    '.php': 'Php',
    '.txt': 'Txt',
}

def list_files(source_dir, preview_callback=None, organize=False):
    """
    source_dir : folder to scan
    preview_callback : function to send file info to GUI
    organize : if True, move files; if False, only preview
    """
    if not os.path.exists(source_dir):
        if preview_callback:
            preview_callback("Invalid Path!")
        else:
            print("Invalid Path!")
        return

    files = []
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        if os.path.isdir(file_path):
            continue
        _, file_ext = os.path.splitext(file)
        files.append({'name': file, 'ext': file_ext})

    get_file_category(files, source_dir, preview_callback, organize)


def get_file_category(files, source_dir, preview_callback=None, organize=False):
    total_files = len(files)
    moved_count = 0

    for index, file in enumerate(files, start=1):
        file_name = file['name']
        category = categories.get(file['ext'], "Others")
        new_path = os.path.join(source_dir, category)

        if organize:
            os.makedirs(new_path, exist_ok=True)
            source_file = os.path.join(source_dir, file_name)

            # Handle duplicates
            name, ext = os.path.splitext(file_name)
            destination = os.path.join(new_path, file_name)
            counter = 1
            while os.path.exists(destination):
                file_name = f"{name}({counter}){ext}"
                destination = os.path.join(new_path, file_name)
                counter += 1

            shutil.move(source_file, destination)
            moved_count += 1

        # Preview / log message
        message = f"[{index}/{total_files}] {file_name} → {category}"
        if preview_callback:
            preview_callback(message)
        else:
            print(message)

    if organize and preview_callback:
        preview_callback(f"\n✅ {moved_count} files organized successfully!")