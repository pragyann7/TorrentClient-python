# Torrent Streamer

This script allows you to download torrents directly using a magnet link.

## Prerequisites

Install `libtorrent-rasterbar` globally using Homebrew:

```bash
brew install libtorrent-rasterbar
```

## Setup

1. Move `torrent.py` to a global folder of your choice.(ie. /Users/username/stream_magnet.py)
2. Edit the `magnet_link` variable in the script and replace it with your desired magnet link.
   *(The current example downloads: "A Knight of the Seven Kingdoms")*

## Usage

1. Open your terminal.
2. Navigate to the folder containing `torrent.py`.
3. Run the script:

```bash
python torrent.py
```

4. After downloading, open the `DOWNLOAD_PATH` folder in Finder.(ie. ./my_torrents)
5. Open the downloaded file and enjoy!
