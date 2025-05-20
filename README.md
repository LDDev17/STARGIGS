# ⭐ Stargigs Backend

Stargigs is a backend application built with **Flask**, **SQLAlchemy**, and **Marshmallow**. It provides a scalable and modular foundation for managing users, authentication, and core features of a gig-based platform.

---

## 📁 Project Structure

```
├── app/
│   ├── blueprints/             # Modular Blueprints for features
│   │   ├── auth/               # Authentication-related routes
│   │   ├── payments/           # Payment-related routes
│   │   ├── performers/         # Performer-related routes
│   │   ├── reviews/            # Review-related routes
│   │   ├── search/             # Search-related routes
│   ├── models/                 # Database models
│   │   ├── client.py           # Example model
│   │   ├── schemas/            # Marshmallow schemas
│   ├── utils/                  # Utility functions and helpers
│   ├── tests/                  # Unit and integration tests
│   ├── __init__.py             # App factory and initialization
├── database.py                 # Database connection and setup
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .trunk/                     # Configuration for linting and formatting
│   ├── trunk.yaml
│   ├── configs/
│   │   ├── .isort.cfg
│   │   ├── .markdownlint.yaml
│   │   ├── ruff.toml
├── instance/                   # Instance-specific files
│   ├── stargigs.db             # SQLite database (example)
```

---

## 🚀 Features

- **User Management**: Create, update, and manage user accounts.
- **Authentication**: Secure login and token-based access using JWT.
- **Payments**: Payment handling logic (in progress or to be integrated).
- **Performer Profiles**: Manage performer-specific data.
- **Reviews**: Users can leave feedback and ratings.
- **Search**: Search functionality across the platform.
- **Modular Structure**: Organized via Flask Blueprints for scalability.

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd stargigs-codingtemple-backend
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
- Ensure `instance/stargigs.db` exists, or
- Configure a custom database in `config.py`.

### 5. Run the Application
```bash
flask run
```

---

## 🌐 Usage

- Access the app at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- The root endpoint (`/`) should display a welcome message or basic info.

---

## 🛠️ Development

### 🧹 Code Formatting & Linting

This project uses:

- **Black** – Python code formatter
- **isort** – Automatically sorts imports
- **Ruff** – Fast Python linter

Run them with:
```bash
black .
isort .
ruff .
```

### ✅ Testing

Add your tests in `app/tests/` and run them using:
```bash
pytest
```

---

## 📊 API Endpoints

### Authentication
- `POST /auth/login`: User login and token generation.
- `POST /auth/register`: User registration.

### Bookings
- `POST /bookings`: Create a new booking (requires authentication).
- `PUT /bookings/<id>`: Update an existing booking (requires authentication).
- `DELETE /bookings/<id>`: Cancel a booking (requires authentication).
- `GET /bookings/<id>`: Retrieve booking details (requires authentication).

### Performers
- `GET /performers`: List all performers.
- `GET /performers/<id>`: Retrieve performer details.

---

## 🤝 Contributing

1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Open a pull request with clear documentation and reasoning.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).