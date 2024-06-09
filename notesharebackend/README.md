
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

3. **Create a new Django project**:
    ```sh
    django-admin startproject myproject
    cd myproject
    ```

4. **Create a new Django app**:
    ```sh
    python manage.py startapp myapp
    ```

## Step 2: Configure the Django Project

1. **Add the app and REST framework to `INSTALLED_APPS` in `myproject/settings.py`**:
    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'myapp',
    ]
    ```

2. **Create models, serializers, and views** in `myapp` (e.g., `models.py`, `serializers.py`, `views.py`).

3. **Add URLs** in `myapp/urls.py` and include them in the project's `urls.py`:
    ```python
    from django.urls import path, include
    from myapp import views

    urlpatterns = [
        path('user/', views.UserViewSet.as_view()),
        path('login/', views.UserLoginView.as_view()),
        path('register/', views.UserRegisterView.as_view()),
        path('users/', views.AllUsersView.as_view()),
    ]
    ```
    In `myproject/urls.py`:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('myapp.urls')),
    ]
    ```

## Step 3: Set Up Google Cloud Storage

1. **Install the Google Cloud Storage client library**:
    ```sh
    pip install google-cloud-storage
    ```

2. **Create a service account** in the Google Cloud Console and download the JSON key file.

3. **Set up Google Cloud Storage in your Django settings**:
    ```python
    # In myproject/settings.py
    from google.oauth2 import service_account

    GOOGLE_CREDENTIALS = service_account.Credentials.from_service_account_file(
        '/path/to/your/service-account-file.json'
    )

    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'your-bucket-name'
    GS_CREDENTIALS = GOOGLE_CREDENTIALS
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


# 1 . API'S Documentation

## UserViewSet

**Description:** This endpoint retrieves user information using the token sent with the request.

- **URL:** `/user/`
- **Method:** `GET`
- **Permissions required:** `IsAuthenticated`
- **Authentication required:** `TokenAuthentication`

**Response:**
- **Status 200:** User information in JSON format.
- **Status 404:** User not found.

## UserLoginView

**Description:** This endpoint handles the login of the user.

- **URL:** `/login/`
- **Method:** `POST`
- **Permissions required:** `AllowAny`

**Request Body:**
- `username`: string
- `password`: string

**Response:**
- **Status 200:** Token in JSON format.
    - `token`: string

## UserRegisterView

**Description:** This endpoint handles user registration.

- **URL:** `/register/`
- **Method:** `POST`
- **Permissions required:** `AllowAny`

**Request Body:**
- `username`: string
- `email`: string
- `password`: string

**Response:**
- **Status 201:** Token and user information in JSON format.
    - `token`: string
    - `user_id`: integer
    - `email`: string

## AllUsersView

**Description:** This endpoint retrieves all users.

- **URL:** `/users/`
- **Method:** `GET`
- **Permissions required:** `AllowAny`

**Response:**
- **Status 200:** List of users in JSON format.


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

