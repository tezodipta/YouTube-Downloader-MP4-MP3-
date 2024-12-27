# YouTube Downloader (MP4 & MP3)

This Python application allows users to download videos and audio from YouTube in either MP4 or MP3 format. It uses the `pytube` library to fetch the content and `tkinter` for the graphical user interface (GUI).

## Features
- Download YouTube videos in MP4 format with the highest resolution.
- Download YouTube audio as MP3.
- Simple GUI built with `tkinter` for easy interaction.
- Allows users to select the download location using a file dialog.

## Prerequisites
Before running the script, ensure you have the following:
1. Python 3 installed on your system.
2. Install the required libraries:
   - `tkinter`: For the GUI.
   - `pytube`: For downloading YouTube videos.

You can install the necessary libraries using pip:
```bash
pip install pytube
```

## How to Use

1. Clone or download the script to your system.
2. Run the script:
```bash
    python youtube_downloader.py
```
3. The GUI window will appear. Enter the YouTube video URL in the text box.
4. Select the desired format (MP4 or MP3) using the radio buttons.
5. Click the "Download" button to begin downloading the video or audio.
6. A file dialog will appear, allowing you to choose the directory where the file should be saved.
7. After the download is complete, a message box will inform you of the success.

---

## Code Overview

### `download_video()` Function
- Fetches the YouTube video from the provided URL.
- Based on the selected format, either downloads the highest resolution MP4 video or the MP3 audio.
- Displays a success message when the download is complete or an error message if something goes wrong.

### GUI Setup
- Uses `tkinter` to create a simple user interface where users can input the video URL, choose the format, and initiate the download.

---

## Example Usage

1. Open the application.
2. Enter a valid YouTube URL (e.g., `https://www.youtube.com/watch?v=example`).
3. Select "MP4" or "MP3".
4. Click "Download" and choose a download folder.

---

## Notes
- Ensure the YouTube URL is valid before attempting to download.
- The `pytube` library handles the downloading process, so an internet connection is required to fetch the video/audio.
- If the download does not start, check your internet connection or the validity of the YouTube link.
