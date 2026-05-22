from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    system   = data.get('system', '')
    messages = data.get('messages', [])
    if not system or not messages:
        return jsonify({'error': 'system과 messages가 필요합니다.'}), 400
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1000,
            system=system,
            messages=messages
        )
        return jsonify({'text': response.content[0].text})
    except anthropic.AuthenticationError:
        return jsonify({'error': 'API 키가 올바르지 않습니다.'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print("=" * 50)
    print(f"  레드라인 서버 시작 — http://localhost:{port}")
    print("=" * 50)
    app.run(debug=False, host='0.0.0.0', port=port)
