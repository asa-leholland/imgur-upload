import requests
import os
import json
import openpyxl

# Import csv library
import csv
import csv
import openpyxl

# Define a list of strings
string_list = ["string1", "string2", "string3"]


def write_string_list_to_csv(string_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        string_writer = csv.writer(csvfile, delimiter=',')

        for string in string_list:
            string_writer.writerow([string])



def write_csv_to_excel(filename) -> str:
    new_filename = f'{filename[:-4]}_result.xlsx'
    wb = openpyxl.Workbook()
    ws = wb.active

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            ws.append(row)

    wb.save(new_filename)
    return new_filename

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
        if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov") or filename.endswith(".webm") or filename.endswith(".wmv"):
            func(filename)
            count += 1
        else:
            continue
    return count


def attach_vid_to_album(video_id: str, album_id: str):
    api_endpoint = f"https://api.imgur.com/3/album/{album_id}/add"

    data = {
        'ids': video_id
    }

    return requests.post(api_endpoint, headers=HEADERS, data=data)


def get_first_album_video_link(album_id: str):
    url = f"https://api.imgur.com/3/album/{album_id}"
    response = requests.get(url, headers=HEADERS).json()
    return response['data']['images'][0]['link']


def get_album_link(album_id: str):
    return f'https://imgur.com/a/{album_id}'

def upload_video_to_album(album_name: str, album_description: str, video_filename: str):
    print(f'Uploading {video_filename} to album {album_name}...')
    response = create_album(album_name, album_description)
    album_json_response = json.loads(response.text)
    album_id = album_json_response.get("data").get("id")
    print(f'Album created with id {album_id}.')
    response = upload_mp4_to_imgur(video_filename)
    print(response)
    video_json_response = json.loads(response.text)
    video_id = video_json_response.get("data").get("id")
    print(f'Video uploaded with id {video_id}.')
    attach_vid_to_album(video_id, album_id)
    print(f'Video attached to album.')
    return get_album_link(album_id)


def strip_extension(filename: str) -> str:
    return filename[:filename.rfind('.')] if '.' in filename else filename


def build_excel_file_of_imgur_album_links(video_directory: str, output_filename: str) -> str:
    url_strings = []
    iterate_through_vids(
        video_directory,
        lambda filename: url_strings.append(
            upload_video_to_album(
                f'Album for {strip_extension(filename)}',
                'N/A',
                f'{video_directory}/{filename}',
            )
        ),
    )
    csv_filename = f'{output_filename}.csv'
    write_string_list_to_csv(url_strings, csv_filename)
    return write_csv_to_excel(csv_filename)


def delete_album(album_id: str):
    url = f"https://api.imgur.com/3/album/{album_id}"
    return requests.delete(url, headers=HEADERS)


def get_all_album_ids():
    url = f"https://api.imgur.com/3/account/me/albums/ids"
    response = requests.get(url, headers=HEADERS).json()
    return response['data']

def delete_all_albums():
    album_ids = get_all_album_ids()
    for album_id in album_ids:
        delete_album(album_id)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: python3 main.py <video_directory> <output_filename>')
    build_excel_file_of_imgur_album_links(sys.argv[1], sys.argv[2])
