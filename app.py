from flask import Flask, request, jsonify
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

# Cấu hình Cloudinary


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    result = cloudinary.uploader.upload(file)
    return jsonify({"url": result['secure_url']})

if __name__ == "__main__":
    app.run(debug=True)
