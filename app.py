import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-persona', methods=['POST'])
def generate_persona():
    data = request.json
    user_input = data.get('prompt', '')
    
    # 🚀 Mock Response: Bypassing Google's server to show you your working UI!
    mock_persona = f"""
    <h3>🎯 Target Customer Persona for: {user_input}</h3>
    <ul>
        <li><strong>Demographics:</strong> Age 22-35, Tech-savvy urban professionals and students.</li>
        <li><strong>Psychographics:</strong> Values efficiency, loves automated tools, easily frustrated by broken workflows or slow setups.</li>
        <li><strong>Pain Points:</strong> Spends too much time on repetitive tasks; struggles with complex cloud platform setups and API restrictions.</li>
        <li><strong>Buying Behavior:</strong> Prefers clean user interfaces, values quick "jugaad" solutions, highly active on digital learning platforms.</li>
    </ul>
    """
    
    # Instantly returns success without calling the API
    return jsonify({"success": True, "persona": mock_persona})

if __name__ == '__main__':
    app.run(debug=True, port=5001)