# LibraryAssembler

Welcome to **LibraryAssembler**! This project is in its early stages and aims to build a modern, versatile digital library organizer that can handle not only eBooks, but also magazines, audiobooks, comics, and potentially newspapers. The goal is to create a powerful, intuitive, and feature-rich solution for organizing and discovering digital content.

## Project Overview

**LibraryAssembler** is an open-source initiative to redefine how digital libraries are managed. Taking inspiration from tools like Sonarr and Radarr, the project focuses on automating the organization, discovery, and management of digital content across various formats.

Currently in the planning and development phase, the project welcomes input, ideas, and contributions to help shape its future. Whether you're a developer, designer, or simply passionate about digital content, your involvement is highly valued.

## Tech Stack

To ensure flexibility and scalability, the project employs a lightweight, modular tech stack:

- **Backend:** Flask (Python)
- **Frontend:** React (planned for the web UI)
- **Database:** SQLAlchemy ORM with SQLite for development and PostgreSQL for production
- **Testing & Quality Assurance:** Pytest + Flake8
- **CI/CD:** GitHub Actions

## Project Status
- **Planning and Design**: Currently focused on defining core features, architecture, and user experience. This is the perfect stage for contributors to share ideas and guide the projects development.
- **Feature Ideas**:
  - **Automated Library Organization**: System for sorting and categorizing content using metadata, series, and custom tags.
  - **Metadata Management**: Methods for retrieving and updating metadata for a diverse range of content types.
  - **Collection and Series Management**: Tools to organize and manage collections, series, volumes, and issues effectively.
  - **Custom Tagging and Filters**: User-friendly tagging and robust filtering for content personalization.
  - **User Interface Design**: Development of responsive, mobile-friendly web interfaces with a focus on ease of use and accessibility.

## Getting Involved

Since this project is still in its infancy, there are numerous ways to contribute:

- **Share Your Ideas**: Have a feature in mind or think something can be improved? [Open an issue](https://github.com/crow50/libraryassembler/issues) on GitHub to contribute.
- **Join the Conversation**: Collaborate with the community on the [Discussions](https://github.com/crow50/libraryassembler/discussions) tab.
- **Contribute to Code**: Explore open issues or propose new ones. Early-stage contributions will help lay a strong foundation.
- **Help with Documentation**: Assist in creating clear, comprehensive documentation to support future contributors and users.

### Setting Up the Project for Development

Heres how to start contributing to the LibraryAssembler project:

1. Clone the Repository:
   ```bash
   git clone https://github.com/crow50/libraryassembler.git
   cd libraryassembler
   ```

2. Set Up the Virtual Environment (Python):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install Dependencies:
   ```bash
   pip install -e .
   ```

4. Start Developing: Explore the codebase and begin contributing to the projects structure.

## Backend Application

LibraryAssembler includes a minimal Flask application that forms the basis for advanced ingestion and automation features. The application files reside in the `src/libraryassembler/` directory and provide a standard application factory (`create_app`).

### Running the Development Server

1. Set the Flask application module:
   ```bash
   export FLASK_APP=libraryassembler.app
   ```

2. Initialize the database (creates an SQLite database in the project root by default):
   ```bash
   flask --app libraryassembler.app init-db
   ```

3. Start the development server:
   ```bash
   flask --app libraryassembler.app run --debug
   ```

Verify the service using the bundled health-check endpoint:

```bash
curl http://127.0.0.1:5000/api/health
```

The default configuration uses `libraryassembler.db` to store data. You can override this location by setting the `DATABASE_URL` environment variable before running the application.

### Running Tests

LibraryAssembler comes with a minimal test suite to validate critical components such as the Flask factory and database initialization. To execute the tests, run:

```bash
pytest
```

## Project Structure

As the project evolves, so will its structure. The current organization includes:

- **`src/`**: Core functionalities, integration points, and UI components.
- **`docs/`**: Developer and user documentation.
- **`tests/`**: Unit and integration tests.

## Contributing

Your contribution is crucial for building LibraryAssembler into a robust digital library organizer. Whether you focus on code, design, documentation, or brainstorming concepts, your input is vital.

Check out the [Contribution Guide](CONTRIBUTING.md) for detailed instructions on getting started.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or suggestions, please [open an issue](https://github.com/crow50/libraryassembler/issues) or engage with the community on the [Discussions](https://github.com/crow50/libraryassembler/discussions) page in the repository.