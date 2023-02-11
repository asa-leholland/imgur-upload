import json
from main import create_album, iterate_videos
import os

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



def iterate_through_vids(directory, func):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".webm"):
            func(filename)
        else:
            continue


# Pytest Skeletons

# Test 1: Iterate through each video file provided


def test_iterate_through_vids():
    iterate_through_vids
    # code to iterate through each video file here
        # get a list of all the video files in the directory
    video_list = os.listdir(directory)

    # loop through the list and call func with each file
    for video in video_list:
        func(video)

    # assert that func was called with every file
    assert len(video_list) == func.call_count

# Test 2: Upload each video file to Imgur


def test_upload_to_imgur():
    # code to upload each video file to Imgur here
    raise AssertionError
# Test 3: Check response status codes to ensure successful video uploads


def test_check_response_status():
    # code to check response status code here
    raise AssertionError
# Test 4: Copy-paste each URL to Excel


def test_copy_paste_urls_to_excel():
    # code to copy-paste each URL to Excel here
    raise AssertionError
# Test 5: Validate that each URL follows proper structure (https://imgur.com/a/)


def test_validate_url_structure():
    # code to validate URL structure here
    raise AssertionError
# Test 6: Embed URLs into Reddit


def test_embed_urls_into_reddit():
    # code to embed URLs into Reddit here
    raise AssertionError
# Test 7: Verify videos successfully embedded in Reddit


def test_verify_videos_embedded():
    # code to verify videos are successfully embedded in Reddit here
    raise AssertionError
