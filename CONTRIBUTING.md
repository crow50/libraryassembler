# Contribution Guide

Thank you for your interest in contributing to LibraryAssembler! To ensure a smooth contribution process, please follow these steps:

## Getting Started

### 1. Clone the Repository
First, clone the repository to your local machine using the following command:
```bash
git clone https://github.com/yourusername/LibraryAssembler.git
cd LibraryAssembler
```

### 2. Set Up a Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies. Follow these steps to set up:  
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

After activation, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run Tests
Make sure your changes do not break existing functionality. Run the tests to verify:
```bash
pytest
```

## Making Changes
1. Start by checking out a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

3. Push your branch to the remote repository:
   ```bash
   git push origin feature/your-feature-name
   ```

## Opening a Pull Request
1. Go to the [GitHub repository](https://github.com/yourusername/LibraryAssembler).
2. Click on **"New pull request"**.
3. Select your branch and provide a clear and descriptive title and description for your pull request.
4. Submit your pull request.

## Code Review Process
Your pull request will be reviewed by maintainers to ensure quality and alignment with the project's goals. Please address any feedback from reviewers promptly.

Thank you for your contributions!