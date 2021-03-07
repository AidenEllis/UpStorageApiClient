## UpStorageClientApi

### UpStorage Service Api.

* `Uploading Files`
* `Validating Cerdentails`
* `Listing Files`

<br>

## Installation

1. Get a free API Key at [https://example.com](https://example.com)

2. Install Library Using `pip`
   ```shell script
   python3 pip install UpStorageApiClient
   ```
3. Or Download Files With Git
   ```sh
   git clone https://github.com/user/repo
   ```
4. Import Class
   ```python
   from UpStorageApiClient.api import UpStorageBucket
   ```
5. Authenticate with the api
   ```python
   bucket = UpStorageBucket(auth_token, api_key)
   ```
6. Make A Request In This Case `upload`
   ```python
   bucket.upload(file_path='test.txt', is_private=True)
   
   
   Output: {'file': 'https://example/file.txt/'}
   ```
   `file_path: path of the file you want to upload.`
   `is_private: file types: [public, private] Default: False`
7. Get All `File` From Bucket
   ```python
   bucket.get_all_files()
   
   Output: {'url': 'https://example/file.png/', 'is_private': 'True', ...}
   ```

