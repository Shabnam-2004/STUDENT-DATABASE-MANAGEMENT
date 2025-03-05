# Student Hub Software

## Overview
Student Hub is a modern, user-friendly student management software built with Python using the Tkinter library for the GUI and a MySQL database for data storage. The software enables users to manage student records efficiently with features like adding, updating, deleting, and viewing student details.

## Features
- Modern UI built with Tkinter
- Database integration using MySQL (pymysql)
- Student record management (CRUD operations)
- Validation for inputs (contact, address, full name)
- Calendar widget for date selection
- Image support using PIL (Pillow)

## Technologies Used
- **Python** (Tkinter for GUI)
- **MySQL** (pymysql for database management)
- **Pillow (PIL)** (for image handling)
- **tkcalendar** (for date selection)
- **Custom validation module** (validate.py for input validation)

## Installation
### Prerequisites
Ensure you have Python installed on your system. Install the required dependencies using pip:

```sh
pip install pymysql pillow tkcalendar
```

### Database Setup
1. Create a MySQL database and table structure for storing student records.
2. Update the database connection settings in the script.

## Usage
Run the main Python script to launch the Student Hub application:

```sh
python student_hub.py
```

## Folder Structure
```
📁 StudentHub
├── 📄 main.py  # Main application script
├── 📄 validate.py      # Input validation module
├── 📄 README.md        # Project documentation
├── 📁 icon           # UI images and assets
```

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or contributions, please reach out via GitHub or email.

---
Developed by **SHABNAM YADAV**

