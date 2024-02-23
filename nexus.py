import os
import requests

# Get the current directory
current_directory = os.getcwd()

# Define the directory path relative to the current directory
directory_path = os.path.join(current_directory, 'packages/raw/')

# Define the parameters
params = (
    ('repository', 'hosted-raw'),  # Repository name
)

# Define the files to upload
files = {
    'raw.asset1': ('zap-alerts.txt', open('zap-alerts.txt', 'rb')),  # Adjust file name and path accordingly
    'raw.asset2': ('zap-alerts-world.txt', open('zap-alerts-world.txt', 'rb')),  # Adjust file name and path accordingly
}

# Define additional data
data = {
    'raw.directory': directory_path,  # Adjust directory path if necessary
    'raw.asset1.filename': 'zap-alerts.txt',  # Adjust file name accordingly
    'raw.asset2.filename': 'zap-alerts-world.txt',  # Adjust file name accordingly
}

# Make the POST request
response = requests.post('http://localhost:8081/service/rest/v1/components?repository=zap-reports', params=params, files=files, data=data, auth=('admin', '12345678'))

# Check the response status code
if response.status_code == 204:
    print("Files uploaded successfully!")
else:
    print(f"Failed to upload files. Status code: {response.status_code}")
