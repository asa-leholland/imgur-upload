import requests


def create_album(album_title: str, album_description: str):
    imgur_api_link = "https://api.imgur.com/3/album"
    headers = {
        "Authorization": 'Bearer 1496d3942360d35e663fe0ae248b3d117c154062'
        }

    privacy = "private"
    layout = "blog"

    data = {
        "title": album_title,
        "description": album_description,
        "privacy": privacy,
        "layout": layout
    }
    return requests.post(imgur_api_link, headers=headers, data=data)
