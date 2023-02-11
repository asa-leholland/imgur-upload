import json
from main import create_album, iterate_through_vids, upload_mp4_to_imgur, upload_video_to_album, write_string_list_to_csv, write_csv_to_excel
import os
import openpyxl
from pathlib import Path


def test_create_album():
    ALBUM_NAME = "Test album"
    ALBUM_DESCRIPTION = "Test album description"
    response = create_album(ALBUM_NAME, ALBUM_DESCRIPTION)
    assert response.status_code == 200
    json_response = json.loads(response.text)
    assert json_response.get("success") is True
    assert json_response.get("status") == 200
    assert json_response.get("data").get("id") is not None
    assert json_response.get("data").get("deletehash") is not None


def test_iterate_through_vids():
    count = iterate_through_vids("samples", print)
    video_list = os.listdir("samples")
    assert len(video_list) == count


def test_upload_to_imgur():
    VIDEO_FILENAME = "samples/file_example_AVI_480_750kB.avi"
    response = upload_mp4_to_imgur(VIDEO_FILENAME)
    assert response.status_code == 200
    json_response = json.loads(response.text)
    assert json_response.get("success") is True
    assert json_response.get("status") == 200
    assert json_response.get("data").get("id") is not None
    assert json_response.get("data").get("deletehash") is not None
    assert json_response.get("data").get("link") is not None


def test_upload_to_album():
    ALBUM_NAME = "Test an album with a video"
    ALBUM_DESCRIPTION = "Test album description"
    VIDEO_FILENAME = "samples/file_example_AVI_480_750kB.avi"
    link_to_video_in_album = upload_video_to_album(ALBUM_NAME, ALBUM_DESCRIPTION, VIDEO_FILENAME)
    assert '/a' in link_to_video_in_album



def test_add_to_excel():
    strings = ['test1', 'test2', 'test3']
    input_file_name = 'test_file.csv'
    write_string_list_to_csv(strings, input_file_name)
    excel_filename = write_csv_to_excel(input_file_name)
    assert Path(excel_filename).is_file()
    assert openpyxl.load_workbook(excel_filename).active.max_row == len(strings)
    assert openpyxl.load_workbook(excel_filename).active['A1'].value == strings[0]
    os.remove(input_file_name)
    os.remove(excel_filename)



def test_end_to_end_excel_file():
