
# Play YouTube video using Python
import webbrowser

try:
    song = input("Enter Song Name: ")
    search_url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
    webbrowser.open(search_url)
    print("Successfully opened YouTube search results")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Download YouTube video using Python
import yt_dlp

url = input("Enter video url:")
ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully")