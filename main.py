import requests
import os

BASE_IMGUR_API_URL = 'https://api.imgur.com/3/'
HEADERS = {'Authorization': 'Bearer 1496d3942360d35e663fe0ae248b3d117c154062'}


def create_album(album_title: str, album_description: str):
    imgur_api_link = f"{BASE_IMGUR_API_URL}album"

    privacy = "private"
    layout = "blog"

    data = {
        "title": album_title,
        "description": album_description,
        "privacy": privacy,
        "layout": layout
    }
    return requests.post(imgur_api_link, headers=HEADERS, data=data)


def upload_image_to_imgur(filename: str):
    api_upload_endpoint = f'{BASE_IMGUR_API_URL}image'
    image_binary = open(filename, 'rb').read()

    data = {
        "image": image_binary
    }
    return requests.post(api_upload_endpoint, headers=HEADERS, data=data)


def upload_mp4_to_imgur(filepath: str, album_id: str = None):
    url = f"{BASE_IMGUR_API_URL}upload"
    payload = {
        'album': album_id,
        'type': 'file',
        'disable_audio': '0'
        }
    files = [
        ('video', open(filepath, 'rb'))
    ]
    return requests.request("POST", url, headers=HEADERS, data=payload, files=files)


def iterate_through_vids(directory, func) -> int:
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov") or filename.endswith(".ogg") or filename.endswith(".webm") or filename.endswith(".wmv"):
            func(filename)
            count += 1
        else:
            continue
    return count
