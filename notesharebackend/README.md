
# Setting Up and Running the Django Server

## Step 1: Install Django and Django REST Framework

1. **Create a virtual environment** (optional but recommended):
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

2. **Install Django and Django REST framework**:
    ```sh
    pip install django djangorestframework
    ```


## Step 2: Set Up Google Cloud Storage

1. **Install the Google Cloud Storage client library**:
    ```sh
    pip install google-cloud-storage
    ```

3. **Set up Google Cloud Service key to the GOOGLE_CREDENTIALS variable(Dont push the service key it is a secret)**:
    ```python
    export GOOGLE_CREDENTIALS='/path/to/your/service-account-file.json'
    ```

4. **Install Django storage package**:
    ```sh
    pip install django-storages
    ```

5. **Add `storages` to `INSTALLED_APPS`**:
    ```python
    INSTALLED_APPS = [
        ...
        'storages',
    ]
    ```
## Step 3: Configure the database using sql version >= 8.0
1 **Using the setupdb.sql**:
    `` cat setupdb.sql | mysql -u root -p ``

## Step 4: Run the Django Server

1. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

2. **Create a superuser** (optional but useful for accessing the admin site):
    ```sh
    python manage.py createsuperuser
    ```

3. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

Your Django server should now be up and running, with REST API endpoints and Google Cloud Storage configured.


# 1. User API'S Documentation

## UserViewSet

**Description:** This endpoint retrieves user information using the token sent with the request.

- **URL:** `api/get_user/`
- **Method:** `GET`
- **Permissions required:** `IsAuthenticated`
- **Authentication required:** `TokenAuthentication`

**Response:**
- **Status 200:** User information in JSON format.
- **Status 404:** User not found.

#### Example Request
```bash
curl -X GET -H "Authorization: Token <your-token>"  http://127.0.0.1:8000/api/get_user/
```

## UserLoginView

**Description:** This endpoint handles the login of the user.

- **URL:** `api/login/`
- **Method:** `POST`
- **Permissions required:** `AllowAny`

**Request Body:**
- `username`: string
- `password`: string

**Response:**
- **Status 200:** Token in JSON format.
    - `token`: string

#### Example Request
```bash
 curl -X POST -H "Content-Type: application/json" -d '{"username": "<your_username>", "password": "<your_password"}' http://127.0.0.1:8000/api/login/
```

## UserRegisterView

**Description:** This endpoint handles user registration.

- **URL:** `/api/signup/`
- **Method:** `POST`
- **Permissions required:** `AllowAny`

**Request Body:**
- `username`: string
- `email`: string
- `first_name`: string
- `last_name`: string
- `password`: string

**Response:**
- **Status 201:** Token and user information in JSON format.
    - `token`: string
    - `user_id`: integer
    - `email`: string

#### Example Request
```bash
  curl -X POST -H "Content-Type: application/json" -d '{"username": "<your_username>", "email": "<your_email@gmail.com>", "first_name": "<first_name>", "last_name": "<last_name>", "password":"<your_password>"}' http://127.0.0.1:8000/api/signup/
```


## AllUsersView

**Description:** This endpoint retrieves all users.

- **URL:** `api/all_users/`
- **Method:** `GET`
- **Permissions required:** `AllowAny`

**Response:**
- **Status 200:** List of users in JSON format.

#### Example Request
```bash
curl -X GET   http://127.0.0.1:8000/api/all_users/
```

# 2. FILES API'S Documentation

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

