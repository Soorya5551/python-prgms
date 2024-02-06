import sys
sys.path.append(r'C:\xampp\htdocs\INTERNSHIP')

from utils import mysqlutility

# Create a connection using utility function
connection = mysqlutility.create_connection()

# Read records
mysqlutility.read_records(connection)

# Update record
mysqlutility.update_record(connection, 'kp', '25')

# Delete record
mysqlutility.delete_record(connection, 'soorya')

# Read records again
mysqlutility.read_records(connection)

# Close the connection
if connection.is_connected():
    connection.close()
    print("Connection closed.")
