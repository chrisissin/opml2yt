from flask import Flask, request, render_template, redirect, url_for, session
import xml.etree.ElementTree as ET
from googleapiclient.discovery import build

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

def parse_opml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    urls = []

    for outline in root.findall('.//outline'):
        url = outline.get('xmlUrl') or outline.get('htmlUrl')
        if url:
            urls.append(url)
    
    return urls

def search_and_subscribe(youtube, channel_name):
    request = youtube.search().list(
        q=channel_name,
        part="snippet",
        type="channel",
        maxResults=1
    )
    response = request.execute()

    if response['items']:
        channel_id = response['items'][0]['id']['channelId']
        print(f"Subscribing to {channel_name} with channel ID: {channel_id}")
        # Placeholder for subscription code
        return f"Subscribed to {channel_name}"
    else:
        print(f"No YouTube channel found for {channel_name}")
        return f"No channel found for {channel_name}"

@app.route('/', methods=['GET', 'POST'])
def get_api_key():
    if request.method == 'POST':
        session['API_KEY'] = request.form['api_key']
        return redirect(url_for('upload_file'))
    return render_template('apikey.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'API_KEY' not in session:
        return redirect(url_for('get_api_key'))
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            youtube = build('youtube', 'v3', developerKey=session['API_KEY'])
            urls = parse_opml(file)
            results = []
            for url in urls:
                # Extract the channel name from the URL (adjust this part based on your OPML structure)
                channel_name = url.split("/")[-1]
                result = search_and_subscribe(youtube, channel_name)
                results.append(result)
            return render_template('result.html', results=results)
    
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
