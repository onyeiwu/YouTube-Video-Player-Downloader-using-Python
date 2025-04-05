# YouTube-Video-Player-Downloader-using-Python
YouTube Video Player &amp; Downloader using Python

 ## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Installation](#️-installation)
- [Usage](#-usage)
  - [1. Play a YouTube Song or Video](#1-play-a-youtube-song-or-video)
  - [2. Download a YouTube Video](#2-download-a-youtube-video)
- [Example Output](#-example-output)
- [Configuration & Customization](#-configuration--customization)
- [Code](#-code)
- [Technologies Used](#-technologies-used)
- [Use Cases](#-use-cases)
- [Best Practices](#-best-practices)
- [Tips & Best Practices](#-tips--best-practices)
- [Contributing](#-contributing)
- [License](#-license)

  ---

## 📖 Overview

This project combines the power of the `webbrowser` module with `yt_dlp` to create a command-line YouTube utility that allows users to:
- Instantly search and **play** YouTube videos in their browser.
- Seamlessly **download** videos from YouTube by entering their URL.

Perfect for those who want quick access to media content without navigating manually through the browser.

---

## ✨ Features

- Command-line interface (CLI)
- Dynamic YouTube search & play
- Download videos using just the URL
- Supports various YouTube formats
- Lightweight, no GUI or heavy dependencies
- Beginner-friendly  

---

## ⚙️ Installation

Make sure you have `Python 3.6+` installed.

Install the required dependency:

```bash
pip install yt-dlp
```
Optionally, install `ffmpeg` to allow `yt_dlp` to convert video/audio formats:

- Windows: https://ffmpeg.org/download.html

- macOS: `brew install ffmpeg`

- Linux: `sudo apt install ffmpeg`

## 🚀 Usage
🔎 1. Play a YouTube Song or Video

Run the script and enter the video/song title when prompted:
```bash
python youtube_tool.py
```
Example:
```text
Enter Song Name: asake lonely at the top
```
This opens YouTube search results for your query in the default browser.

2. Download a YouTube Video

When prompted:
```text
Enter video url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
The video will be downloaded to your current working directory.

You can customize the output directory and format under yt_dlp options (see 🔧 [Configuration](#-configuration--customization)).

Example Output:
```text
Enter Song Name: asake lonely at the top
Successfully opened YouTube search results

Enter video url: https://www.youtube.com/watch?v=abcdefghijk
[youtube] abcdefghijk: Downloading webpage
[youtube] abcdefghijk: Downloading video info webpage
[download] Destination: city_boys.mp4
[download] 100% of 4.95MiB in 00:02
Video downloaded successfully
```
## 🔧 Configuration & Customization
You can customize how videos are downloaded using `yt_dlp`  options:
```python
ydl_opts = {
    'format': 'best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'quiet': False,
    'no_warnings': True
}
```
More options here: [yt_dlp documentation](https://github.com/yt-dlp/yt-dlp#documentation)

## 🧠 Code
```python
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
```
## 🛠 Technologies Used
- `webbrowser` – Opens URLs in default browser
- `yt_dlp` – Enhanced YouTube downloader
- `Python 3.x` – Core programming language

##💡 Use Cases
 - Quick access to YouTube music without typing in browser
 - Download tutorial videos for offline learning
 - Extract and archive video content from lectures/webinars
 - Automate video collection scripts

## 📈 Best Practices
- Ensure stable internet connection before use
- Always verify YouTube's terms of service when downloading content
- Consider organizing downloads into folders using outtmpl
- Use `ffmpeg` with `yt_dlp` for audio/video conversions

## 📥 To-Do & Future Enhancements
 - Add GUI interface for non-technical users
 - Enable audio-only download
 - Support downloading full playlists
 - Add progress bar via `tqdm`
 - Logging and error handling improvements

## 🤝 Contributing
Got a suggestion or found a bug?
Feel free to fork the repo, open an issue, or submit a pull request!

## 📄 License
This project is open-source under the MIT License – use it freely and respectfully.














