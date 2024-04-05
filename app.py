from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the URL of your Django server endpoint
django_url = 'https://fyp-server-django.onrender.com/api/data/gsm/'

@app.route('/receive_data', methods=['POST'])
def receive_data():
    try:
        # Get JSON data from the POST request
        data = request.json

        # Forward the received JSON data to the Django server
        response = requests.post(django_url, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            return jsonify({"message": "Data forwarded successfully to Django server"}), 200
        else:
            return jsonify({"error": f"Failed to forward data to Django server. Status code: {response.status_code}"}), response.status_code

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
