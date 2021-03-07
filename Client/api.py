import requests


class UpStorageBucket:
    """
    Api Client For UpStorage Rest Api.
    """

    def __init__(self, auth_token, api_key):
        self.api_host = 'http://127.0.0.1:8000'
        self.upload_url = f'{self.api_host}/api/storage/upload/'
        self.file_list_url = f'{self.api_host}/api/storage/file/all/'
        self.auth_token = auth_token
        self.api_key = api_key
        self.auth_header = {
            'Authorization': f"Token {str(self.auth_token)}",
            'x-api-key': str(self.api_key)
        }

    def upload(self, file_path, is_private=False):
        """
        Uploads File To UpStorage Server Using Their Api.
        :param file_path: path of the file that you want to send
        :param is_private: Value of File Model of Upstorage [private, public] (default: False)
        :return: This Will Return The Url Of The File.
        """

        headers = self.auth_header

        files = {
            'file': open(file_path, 'rb')
        }

        data = {
            'is_private': is_private
        }

        response = requests.post(self.upload_url, headers=headers, files=files, data=data)

        if self.validate_response(response):
            return response.json()

    def get_all_files(self):
        """
        This Will Get All The Files Of The Project Bucket.
        :return: List Of Files (is_private, url)
        """

        headers = self.auth_header

        response = requests.get(self.file_list_url, headers=headers)
        if self.validate_response(response):
            return response.json()

    @staticmethod
    def validate_response(response):
        """
        Validates Response Codes.Use This Before Doing Any Calls.
        :param response: requests.response obj
        :return: Boolean
        """

        if response.status_code == 401:
            print("UPSTORAGE: Invalid Authorization Token [401]")
            return False
        elif response.status_code == 403:
            print("UPSTORAGE: Invalid Api Key [403]")
            return False
        else:
            return True
