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
More options here: yt_dlp documentation













