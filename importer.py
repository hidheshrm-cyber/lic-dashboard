import zipfile
import os
import shutil

def extract_zip(zip_path):

    extract_folder = "extracted"

    if os.path.exists(extract_folder):
        shutil.rmtree(extract_folder)

    os.makedirs(extract_folder)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

    return extract_folder
