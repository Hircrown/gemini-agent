import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    result = []
    if not full_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        sub_elements = os.listdir(full_path)
        for elm in sub_elements:
            elm_path = os.path.join(full_path, elm)
            size = os.path.getsize(elm_path)
            is_dir = os.path.isdir(elm_path)
            result.append(f"- {elm}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(result)
    except Exception as e:
        return f"Error {e}"
    

