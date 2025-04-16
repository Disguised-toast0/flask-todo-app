# ToDoer

ToDoer is a task management web application built with Flask, SQLAlchemy, and Bootstrap. This application enables users to create, manage, and organize daily tasks through a clean and intuitive interface.

## Overview

ToDoer provides essential task management functionality including task creation, editing, and deletion with an AJAX-powered interface that minimizes page reloads for a smooth user experience.

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/todoer.git
cd todoer
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

5. Access the application at `http://localhost:5000`

## Project Structure

```
todoer/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── static/                # Static files (CSS, JS, images)
├── templates/             # Jinja2 templates
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Usage

### Task Management
- Create tasks by entering title and description
- Update existing tasks via the update interface
- Delete tasks with single-click functionality (AJAX-enabled)
- View task creation dates

### Development
- The application uses SQLite for data storage
- Templates are built with Jinja2 and Bootstrap 3.7.7
- AJAX functionality is implemented with jQuery

## Contributing

1. Fork the repository
2. Create a branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

Your Name - email@example.com

Project Link: https://github.com/yourusername/todoer
