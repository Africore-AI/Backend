# ScholMatch Backend

Welcome to the ScholMatch backend repository! This project provides the backend infrastructure for ScholMatch, a generative AI-based scholarship matching system. The backend handles API requests, manages user data, integrates with the AI model, and supports the overall functionality of the platform.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
GrantAI is designed to streamline the scholarship application process by providing personalized recommendations and application assistance. This backend repository is built using Django and integrates with Hugging Face Transformers for AI functionalities.

## Features
- **User Management**: Handles user registration, authentication, and profile management.
- **Scholarship Matching**: Interfaces with the AI model to provide personalized scholarship recommendations.
- **Application Guidance**: Assists users in drafting and refining application essays.
- **Database Management**: Manages scholarship data and user profiles with PostgreSQL.

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- Virtualenv (optional but recommended)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/grantai-backend.git
   cd grantai-backend
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**
   Update the `DATABASES` section in `settings.py` with your PostgreSQL credentials.

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

## Usage

### API Endpoints

- **User Registration**
  - **POST** `/api/register/`
  - **Request Body**: `{ "username": "user", "password": "pass", "email": "email@example.com" }`
  - **Response**: `{ "message": "User registered successfully." }`

- **User Login**
  - **POST** `/api/login/`
  - **Request Body**: `{ "username": "user", "password": "pass" }`
  - **Response**: `{ "token": "JWT_TOKEN" }`

- **Get Scholarship Recommendations**
  - **POST** `/api/recommendations/`
  - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
  - **Request Body**: `{ "profile": { "academic_achievements": "details", "financial_needs": "details" } }`
  - **Response**: `{ "recommendations": [ { "scholarship_name": "Name", "details": "Details" } ] }`

- **Submit Application**
  - **POST** `/api/apply/`
  - **Headers**: `Authorization: Bearer <JWT_TOKEN>`
  - **Request Body**: `{ "application_data": "data" }`
  - **Response**: `{ "message": "Application submitted successfully." }`

## Configuration
- **API Keys**: Set your Hugging Face API keys in the environment variables `HUGGINGFACE_API_KEY`.
- **Secret Key**: Update `SECRET_KEY` in `settings.py` for security purposes.
- **Allowed Hosts**: Configure `ALLOWED_HOSTS` in `settings.py` to include your domain or IP address.

## Testing
Run tests using Django’s test framework:
```bash
python manage.py test
```

## Contributing
We welcome contributions to improve GrantAI. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a clear description of the changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README further based on your project's specific details and requirements.
