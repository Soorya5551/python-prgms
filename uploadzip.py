from pymongo import MongoClient
import gridfs
import zipfile
import io

client = MongoClient('mongodb://localhost:27017/')
db = client['db']
fs = gridfs.GridFS(db)

zip_file_path = r'C:\Users\soory\Downloads\sample-large-zip-file.zip'

with open(zip_file_path, 'rb') as file:
    zip_data = file.read()

zip_info = zipfile.ZipInfo('docscollection')
zip_info.compress_type = zipfile.ZIP_DEFLATED

with fs.new_file(filename='files2', content_type='application/zip') as file:
    file.write(zip_data)

print("File uploaded successfully to MongoDB using GridFS.")
print(f"Filename in MongoDB: 'files'")
print(f"Content type: 'application/zip'")
print(f"File size: {len(zip_data)} bytes")

client.close()
