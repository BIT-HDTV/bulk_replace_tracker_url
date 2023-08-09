import os
import bencode
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def write_and_bak_torrent(file, torrent_file_path, torrent_data):
    backup_path = torrent_file_path + '.bak'
    os.rename(torrent_file_path, backup_path)

    with open(torrent_file_path, 'wb') as f:
        f.write(bencode.encode(torrent_data))

    print(f"Modified the announce URL in {file}")

def modify_announce_url(file, torrent_file_path, old_announce_url, new_announce_url):
    try:
        with open(torrent_file_path, 'rb') as f:
            torrent_data = bencode.decode(f.read())

        announce_url = torrent_data.get('announce')

        if announce_url != None and announce_url == old_announce_url:

            torrent_data['announce'] = new_announce_url.encode('latin-1')

            write_and_bak_torrent(file, torrent_file_path, torrent_data)

            return True

        b_announce_url = torrent_data.get(b'announce')
        if b_announce_url != None:
            announce_url = b_announce_url.decode('latin-1')

        if announce_url != None and announce_url == old_announce_url:

            torrent_data[b'announce'] = new_announce_url.encode('latin-1')

            write_and_bak_torrent(file, torrent_file_path, torrent_data)

            return True

        return True
    except Exception as e:
        print(f"Error: Torrent can't be open:  {file}, %s", e)
        return False

def modify_announce_url_resume(file, torrent_file_path, old_announce_url, new_announce_url):
    try:
        with open(torrent_file_path, 'rb') as f:
            torrent_data = bencode.decode(f.read())

        trackers = torrent_data.get(b'trackers')

        changed = False

        if trackers != None and len(trackers) > 0:
            for i in range(len(trackers)):
                announce_urls = trackers[i]

                if len(announce_urls) > 0:
                    for j in range(len(announce_urls)):
                        announce_url = announce_urls[j].decode('latin-1')
                        # print(i, j, announce_url)

                        if announce_url != None and announce_url == old_announce_url:
                            torrent_data[b'trackers'][i][j] = new_announce_url.encode('latin-1')
                            changed = True

        if changed:
            write_and_bak_torrent(file, torrent_file_path, torrent_data)

        return True
    except Exception as e:
        print(f"Error: Torrent can't be open:  {file}, %s", e)
        return False

def main():
    folder_path = input("Enter the folder path containing the .torrent files: ")

    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        return

    old_announce_url = input("Enter the old announce URL to replace: ")
    if not is_valid_url(old_announce_url):
        print("Error: Invalid old announce URL. Please provide a valid URL.")
        return

    new_announce_url = input("Enter the new announce URL: ")
    if not is_valid_url(new_announce_url):
        print("Error: Invalid new announce URL. Please provide a valid URL.")
        return

    # torrents
    files = [f for f in os.listdir(folder_path) if f.endswith('.torrent')]

    for file in files:
        file_path = os.path.join(folder_path, file)
        modify_announce_url(file, file_path, old_announce_url, new_announce_url)

    # qbitorrent resume files
    files = [f for f in os.listdir(folder_path) if f.endswith('.fastresume')]

    for file in files:
        file_path = os.path.join(folder_path, file)
        modify_announce_url_resume(file, file_path, old_announce_url, new_announce_url)

    print('Replace done')

if __name__ == '__main__':
    main()
