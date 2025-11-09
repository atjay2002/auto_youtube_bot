import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_youtube_service(client_secrets_file):
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
        creds = flow.run_console()
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("youtube", "v3", credentials=creds)

def upload(video_path, title, description="Auto-generated tech short", tags=None):
    if tags is None:
        tags = ["Python", "AI", "Tech", "Shorts", "AutoTeech Tamil"]

    service = get_youtube_service("client_secret.json")
    body = {
        "snippet": {"title": title, "description": description, "tags": tags, "categoryId": 28},
        "status": {"privacyStatus": "public"},
    }

    media = MediaFileUpload(video_path)
    response = service.videos().insert(part="snippet,status", body=body, media_body=media).execute()
    print(f"Uploaded video ID: {response['id']}")
