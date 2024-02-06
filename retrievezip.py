from pymongo import MongoClient
import gridfs
import zipfile
import io

client = MongoClient('mongodb://localhost:27017/')
db = client['db']
fs = gridfs.GridFS(db)

file_name_inside_db = 'files'

file_entry = fs.find_one({'filename': file_name_inside_db})

if file_entry:
    print(f"Found the zip file '{file_name_inside_db}' in MongoDB.")

    zip_data = file_entry.read()

    with zipfile.ZipFile(io.BytesIO(zip_data), 'r') as zip_ref:

        extraction_path = r'C:\Users\soory\Downloads\extracted_files'
        zip_ref.extractall(extraction_path)

    print(f"Successfully extracted the contents to '{extraction_path}'.")
else:
    print(f"Could not find the zip file '{file_name_inside_db}' in MongoDB.")

client.close()
