import json
from main import create_album, iterate_through_vids, upload_mp4_to_imgur
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
