# upwork-imgur-upload


# Task

Need help using Imgur's API to accomplish a task
Scripting & Automation
Posted 17 hours ago
Specialized profiles can help you better highlight your expertise when submitting proposals to jobs like these. Create a specialized profile.

Worldwide
Goal is to upload vids in bulk to Imgur.com, copy-paste URL’s to Excel and embed in Reddit.

uploading multiple vids to Imgur at once:
          - creates one album for all uploads: https://imgur.com/a/tNtUR9V
          - individual videos inside the album look like this: https://imgur.com/Cw9fEIN

Problem 1: Reddit only embeds vids properly if it follows this structure: https://imgur.com/a/
and not this: https://imgur.com/

So, we want to automatically upload multiple vids into separate albums so it uses the /a structure.

Problem 2: find a way to copy-paste Imgur URL’s to Excel all at once.

This all seems possible using Imgur’s API here, but I have no coding knowledge to do this myself:

https://apidocs.imgur.com/

# Test Suite

Open virtual env with `source venv/Scripts/activate`

Run `pytest`

## Execution

To run, execute `python3 main.py <video_directory> <output_filename>`