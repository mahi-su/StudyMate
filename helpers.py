def format_text(text):
    return text.strip().capitalize()

def handle_file_upload(uploaded_file):
    if uploaded_file is not None:
        return uploaded_file.read()
    return None

def get_env_variable(var_name):
    import os
    return os.getenv(var_name) or "Variable not found"