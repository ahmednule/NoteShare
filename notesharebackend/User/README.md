
# API Documentation

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
