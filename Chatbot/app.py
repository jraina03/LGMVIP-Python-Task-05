from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Set up your Gemini API key
GEMINI_API_KEY = 'AIzaSyBdqSZMBAmfMkVeB7fDB5iDY0eCGi9zzn4'

# Define the default route to return the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Define the '/api' route to handle POST requests
@app.route('/api', methods=['POST'])
def api():
    # Get the message from the request parameters
    message = request.form['message']
    print("Received message:", message)

    try:
        # Call the Gemini API to generate a response
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'contents': [{
                'parts': [{
                    'text': message
                }]
            }]
        }

        response = requests.post(
            f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}',
            headers=headers,
            json=data
        )
        response.raise_for_status()
        response_data = response.json()

        # Extract the generated response from the Gemini API response
        generated_response = response_data['candidates'][0]['content']['parts'][0]['text'].strip()

        return jsonify({'response': generated_response})
    except Exception as e:
        # Log the error
        app.logger.error(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
