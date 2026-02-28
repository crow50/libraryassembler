# User Guide

## Getting Started

Follow these steps to run LibraryAssembler on your local machine:

### 1. Clone the Repository
Download the project source code using the following command:
```bash
# Clone the repository
git clone https://github.com/crow50/libraryassembler.git

# Navigate into the project directory
cd LibraryAssembler
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate the project dependencies.  
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
pip install -e .
```

### 4. Run the Application
To start the Flask application locally, use the following command:
```bash
flask --app libraryassembler.app run --debug
```

The app will be accessible in your browser at: `http://127.0.0.1:5000/`

## Application Overview and Features

### Main Features:
- **Library Organization:** Automatically organize eBooks, audiobooks, comics, and other digital content by tagging and categorizing based on metadata.
- **Metadata Management:** Retrieve enriched metadata for your library entries from various third-party sources like OpenLibrary.

### Navigating the Application:
1. **Dashboard:** View an organized overview of your digital library.
2. **Search Functionality:** Quickly find relevant titles within the library using titles, tags, or metadata.
3. **Content Details:** Access detailed information about any listed item by selecting its title.

Stay tuned for updates as additional features are planned in upcoming phases.

---

## Frequently Asked Questions

### Can I add more metadata fields?
Yes! Customized tagging and metadata fields are important project goals. Stay updated for future releases.

### How do I report an issue or suggest a feature?
Go to our project repository on [GitHub issues page](https://github.com/crow50/libraryassembler/issues), and follow the detailed guide for submitting issues or feature requests.

### Where can I find technical documentation?
Technical details and contribution guidelines are available in the `docs/` folder of the repository. You can find architecture, metadata, and planning details for developers and contributors alike.

---

For further assistance, please check our discussions forum for help: [LibraryAssembler Discussions](https://github.com/crow50/libraryassembler/discussions).