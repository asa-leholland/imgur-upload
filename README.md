# Bulk Video Uploader for Imgur - Readme

Welcome to the Bulk Video Uploader for Imgur project! This application provides a solution for uploading multiple videos to Imgur, organizing them into albums, generating URLs compatible with Reddit embedding, and facilitating the process of copying Imgur URLs to Excel. This README will guide you through the purpose of the project and how to use it effectively.

## Purpose

The primary goal of this project is to simplify the process of uploading videos to Imgur in bulk and then seamlessly integrating them into Reddit posts. Imgur's API is utilized to automate these tasks, ensuring efficiency and ease of use.

### Key Features

1. **Bulk Video Upload**: The application allows you to upload multiple videos to Imgur simultaneously. These videos are automatically organized into an album, making it convenient to manage related content.

2. **Reddit Embedding Compatibility**: Reddit's video embedding structure requires URLs to follow a specific format. The tool generates Imgur album URLs (https://imgur.com/a/) for embedding videos in Reddit posts, ensuring they are displayed correctly.

3. **Excel Integration**: Copying and pasting Imgur URLs individually to Excel can be time-consuming. This application streamlines the process by providing a solution to copy-paste Imgur URLs to Excel all at once, saving you valuable time.

## Getting Started

To use the Bulk Video Uploader for Imgur, follow these steps:

1. Clone the repository and navigate to the project directory.

2. Create and activate a virtual environment (venv) to isolate dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

Install the required dependencies using pip.

```bash
pip install -r requirements.txt
```
Run the test suite to ensure everything is set up correctly.

```bash
pytest
```

Execute the main script to start uploading videos and generating Imgur URLs.

```bash
python3 main.py <video_directory> <output_filename>
```

Replace <video_directory> with the path to the directory containing your video files and <output_filename> with the desired name for the Excel file where Imgur URLs will be copied.

Contributing
If you'd like to contribute to the project, feel free to fork the repository, make your changes, and submit a pull request. Please ensure that you follow best coding practices and maintain clear documentation.

Conclusion
The Bulk Video Uploader for Imgur project simplifies the process of uploading videos, organizing them, and integrating them into Reddit posts. With its automation features and Excel integration, it saves time and enhances your workflow. If you encounter any issues or have suggestions for improvements, don't hesitate to create an issue or contribute to the project.

Happy uploading!
