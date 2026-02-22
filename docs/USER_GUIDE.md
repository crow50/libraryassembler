# User Guide

## Getting Started

Follow these steps to run LibraryAssembler on your local machine:

### 1. Clone the Repository
Download the project source code using the following commands:
```bash
git clone https://github.com/yourusername/LibraryAssembler.git
cd LibraryAssembler
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies for the project.  
**For Unix/macOS:**
```bash
python3 -m venv env
source env/bin/activate
```
**For Windows:**
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies
Install the necessary dependencies using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
To start the Flask application locally, use the following command:
```bash
flask run
```
The app will be available at `http://127.0.0.1:5000/` by default.