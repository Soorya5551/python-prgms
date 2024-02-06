from pymongo import MongoClient
import gridfs

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['db']
fs = gridfs.GridFS(db)

# Specify the filename you used when storing the zip file
file_name_inside_db = 'files'

# Check if the file exists in the GridFS collection
file_exists = fs.exists({'filename': file_name_inside_db})

# Close the MongoDB connection
client.close()

# Print the result
if file_exists:
    print(f"The zip file '{file_name_inside_db}' exists in MongoDB.")
else:
    print(f"The zip file '{file_name_inside_db}' does not exist in MongoDB.")
