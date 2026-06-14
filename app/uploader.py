import os

def save_uploaded_file(uploaded_file):

    upload_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(upload_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return upload_path