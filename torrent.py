import libtorrent as lt
import time
import os

# === CONFIGURATION ===
MAGNET_LINK = "magnet:?xt=urn:btih:4F36DEAA5DFE655B55F8F1F33A69CC771AEBB2D4"
DOWNLOAD_PATH = "./my_torrents"  # <-- your specific folder

# create folder if it doesn't exist
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# === SESSION SETUP ===
ses = lt.session()
ses.listen_on(6881, 6891)

params = {
    "save_path": DOWNLOAD_PATH,  # save all torrent files here
    "storage_mode": lt.storage_mode_t.storage_mode_sparse,
}

handle = lt.add_magnet_uri(ses, MAGNET_LINK, params)

print("⏳ Fetching metadata...")

# wait for metadata
while not handle.has_metadata():
    time.sleep(1)

info = handle.get_torrent_info()
print("✅ Metadata received:", info.name())

# show the largest file
files = info.files()
largest = max(files, key=lambda f: f.size)
file_path = os.path.join(DOWNLOAD_PATH, largest.path)

print(file_path)

print("\n⏬ Downloading to folder:", DOWNLOAD_PATH)

# download loop
while True:
    s = handle.status()
    print(
        f"\rProgress: {s.progress * 100:5.1f}% | "
        f"↓ {s.download_rate / 1000:6.1f} kB/s | "
        f"Peers: {s.num_peers}",
        end=""
    )
    time.sleep(1)
