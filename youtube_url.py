from flask import Flask, request, jsonify, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

def search_youtube(query):
    random_filename = f"{uuid.uuid4()}"
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': f'{random_filename}.%(ext)s',  # Custom filename with a random UUID
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # You can change the quality if needed
        }],
        'postprocessor_args': [
            '-id3v2_version', '4',  # Use ID3v2.4 tags
        ],
        'prefer_ffmpeg': False,
        'username': 'oauth2',  # OAuth2 username
        'password': '',         # OAuth2 password (empty)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]

        title = result.get('title')
        url = result.get('webpage_url')
        channel = result.get('uploader')
        f_duration = result.get('duration')
        duration = result.get('duration')
        thumbnail = result.get('thumbnail')

        final_filename = f"{random_filename}.mp3"
        # Return the first video's details
        return {
            'title': title,
            'url': url,
            'url_local': f"https://audio.serveo.net/mp3/{final_filename}",
            'channel': channel,
            'f_duration': f"{f_duration // 60}m {f_duration % 60}s",
            'duration': duration,
            'thumbnail': thumbnail
        }

@app.route('/audio', methods=['GET'])
def videos():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        video_details = search_youtube(query)
        return jsonify(video_details)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mp3/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_file(filename)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
