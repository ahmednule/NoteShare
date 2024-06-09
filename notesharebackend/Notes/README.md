
# 1. FILES API'S Documentation

## Authentication
All endpoints require token authentication. Ensure you include the token in the `Authorization` header as `Token <your-token>`.

## Endpoints

### 1. File Upload

#### URL
`POST /api/upload/`

#### Description
Uploads a file to Google Cloud Storage.

#### Request Headers
- `Authorization: Token <your-token>`
- `Content-Type: multipart/form-data`

#### Request Parameters
- `file`: The file to be uploaded.
- `subject`: The subject of the file

#### Response
- `201 Created`: File uploaded successfully.
- `400 Bad Request`: Invalid file data.
- `500 Internal Server Error`: Error during file upload.

#### Example Request
```bash
curl -X POST -H "Authorization: Token <your-token>" -H "Content-Type: multipart/form-data" -F "file=@path/to/your/file" http://127.0.0.1:8000/api/upload/
```

#### Example Response
```json
{
  "message": "File uploaded successfully."
}
```

### 2. File Download

#### URL
`GET /api/download/`

#### Description
Downloads a file from Google Cloud Storage.

#### Request Headers
- `Authorization: Token <your-token>`

#### Request Parameters
- `file_name`: The name of the file to be downloaded (as a query parameter).

#### Response
- `200 OK`: File content is returned as an attachment.
- `400 Bad Request`: File name not provided.
- `404 Not Found`: File not found.

#### Example Request
```bash
curl -X GET -H "Authorization: Token <your-token>" "http://127.0.0.1:8000/api/download/?file_name=example.txt"
```

#### Example Response
Returns the file content as an attachment.

### 3. File Search

#### URL
`GET /api/search/`

#### Description
Returns a list of all files in the Google Cloud Storage bucket.

#### Request Headers
- `Authorization: Token <your-token>`

#### Request Parameters
None.

#### Response
- `200 OK`: List of file names.

#### Example Request
```bash
curl -X GET -H "Authorization: Token <your-token>" http://127.0.0.1:8000/api/search/
```

#### Example Response
```json
[
  "file1.txt",
  "file2.txt",
  "image1.png"
]
```

## Detailed Descriptions

### FileUploadView

Handles file uploads to Google Cloud Storage with the following attributes:
- `parser_classes = [MultiPartParser]`
- `permission_classes = [IsAuthenticated]`
- `authentication_classes = [TokenAuthentication]`

#### POST Method
- Validates the uploaded file using `FileUploadSerializer`.
- Adds metadata to the file.
- Uploads the file to Google Cloud Storage.
- Returns a success message on successful upload.

### FileDownloaderView

Handles downloading of files from Google Cloud Storage with the following attributes:
- `parser_classes = [MultiPartParser]`

#### GET Method
- Requires `file_name` as a query parameter.
- Retrieves and returns the file content as an attachment.

### FileSearchView

Handles listing of all files in Google Cloud Storage.

#### GET Method
- Returns a list of all file names in the bucket.

## Example Error Responses

### Invalid Credentials
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### File Not Found
```json
{
  "error": "File not found."
}
```

### General Error
```json
{
  "error": "Error message"
}
```

These endpoints should help you upload, download, and list files in your Google Cloud Storage bucket, provided the correct authentication token is used.

