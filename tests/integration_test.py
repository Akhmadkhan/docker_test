import requests

filepath = "tests/"
filename = "file.txt"
compared_data_size = 512
URL = "8306_bobokhonov_ax-app-1:5000"


class TestIntegration:
    def test_file_upload(self):
        with open(filepath + filename, "rb") as file:
            original_data = file.read(compared_data_size)

        with open(filepath + filename, "rb") as file:
            files = {"upload_file": file}
            file_upload_ans = requests.post(f"http://{URL}/upload", files=files)

        file_download_ans = requests.get(f"http://{URL}/download/{filename}")
        downloaded_data = next(
            file_download_ans.iter_content(chunk_size=compared_data_size)
        )
        assert original_data == downloaded_data
