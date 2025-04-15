
```markdown
# ⭐ Stargigs Backend

Stargigs is a backend application built with **Flask**, **SQLAlchemy**, and **Marshmallow**. It provides a scalable and modular foundation for managing users, authentication, and core features of a gig-based platform.

---

## 📁 Project Structure

```
├── app/
│   ├── Blueprint/
│   │   ├── auth/
│   │   ├── payments/
│   │   ├── performers/
│   │   ├── reviews/
│   │   ├── search/
│   ├── models/
│   │   ├── client.py
│   │   ├── schemas/
│   ├── utils/
│   ├── tests/
│   ├── __init__.py
├── database.py
├── requirements.txt
├── README.md
├── .trunk/
│   ├── trunk.yaml
│   ├── configs/
│   │   ├── .isort.cfg
│   │   ├── .markdownlint.yaml
│   │   ├── ruff.toml
├── instance/
│   ├── stargigs.db
```

---

## 🚀 Features

- **User Management**: Create, update, and manage user accounts.
- **Authentication**: Secure login and token-based access.
- **Payments**: Payment handling logic (in progress or to be integrated).
- **Performer Profiles**: Manage performer-specific data.
- **Reviews**: Users can leave feedback and ratings.
- **Search**: Search functionality across the platform.
- **Modular Structure**: Organized via Flask Blueprints.

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd stargigs-codingtemple-backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Ensure `instance/stargigs.db` exists, or
   - Configure a custom database in `config.py`.

5. **Run the application**:
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

## 🤝 Contributing

1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Open a pull request with clear documentation and reasoning.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

