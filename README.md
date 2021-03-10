## UpStorageClientApi

### UpStorage Service Api.

* `Uploading Files`
* `Deleting Files`
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
   bucket.upload(file='test.txt', is_private=True)
   
   
   Output: {'file': 'https://example/file.txt/'}
   ```
   `file: path of the file or File Object you want to upload.`
   `is_private: file types: [public, private] Default: False`
   
7. Get All `File` From Bucket
   ```python
   bucket.get_all_files()
   
   Output: {'url': 'https://example/file.png/', 'is_private': 'True', ...}
   ```
8. You can delete File too.But For That You Have to pass the file name.if foldername exists then also that too.This is specificly made for the backend Storage System
   ````python
   bucket.delete(file_name='myfile.txt')
   ````
