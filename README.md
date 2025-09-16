# LibraryAssembler

Welcome to **LibraryAssembler**! This project is in its early stages, and I'm excited to build a modern, versatile digital library organizer that will handle not just eBooks, but also magazines, audiobooks, comics, and potentially newspapers. My goal is to create a powerful, intuitive, and feature-rich solution for organizing and discovering digital content.

## Project Overview

**LibraryAssembler** is an open-source initiative aimed at creating a new standard for managing digital libraries. Inspired by tools like Sonarr and Radarr, this project seeks to automate and enhance the organization, discovery, and management of various types of digital content.

This project is currently in its formation phase, and I am actively seeking input, ideas, and contributions to help shape its direction. Whether you're a developer, designer, or simply passionate about digital content, your involvement is welcome!

## Current Status

- **Planning and Design**: I am currently planning the core features, overall architecture, and user experience. This is the perfect time to get involved if you have ideas or want to contribute to the project's direction.
- **Feature Ideas**:
  - **Automated Library Organization**: Concepts for sorting and categorizing content based on metadata, series, and custom tags.
  - **Metadata Management**: Ideas for retrieving and updating metadata for eBooks, audiobooks, comics, and more.
  - **Collection and Series Management**: Planning how to organize and manage collections, including series, volumes, and issues.
  - **Custom Tagging and Filters**: Brainstorming ways to allow users to categorize and filter their content.
  - **User Interface Design**: Initial wireframes and design ideas for a responsive, mobile-friendly web interface.

## How to Get Involved

Since this project is in its early stages, there are many ways to contribute:

- **Share Your Ideas**: Have a feature in mind? Think something could be done differently? [Open an issue](https://github.com/crow50/libraryassembler/issues) to start a discussion.
- **Join the Conversation**: Check out the [Discussions](https://github.com/crow50/libraryassembler/discussions) tab on GitHub to collaborate with others and help shape the project's future.
- **Contribute Code**: If you're ready to start coding, take a look at the open issues or propose new features. Early contributions can help set the foundation for the project.
- **Documentation**: Help me by contributing to the project documentation, even in these early stages, to ensure everything is clear and accessible.

### Initial Setup

If you're interested in contributing code, here's how to get started:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/crow50/libraryassembler.git
   cd libraryassembler
   ```

2. **Set Up the Virtual Environment** (Python):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies** (to be determined as the project evolves):
   ```bash
   pip install -e .
   ```

4. **Start Developing**: Begin exploring the codebase, or help structure it as we define the initial architecture.

## Backend Application

LibraryAssembler now ships with a minimal Flask application that provides the
foundation for future ingestion and automation features. The code lives under
`src/libraryassembler/` and exposes a standard application factory (`create_app`).

### Running the development server

1. **Set the Flask application module**:
   ```bash
   export FLASK_APP=libraryassembler.app
   ```

2. **Initialise the database** (creates an SQLite database in the project root by default):
   ```bash
   flask --app libraryassembler.app init-db
   ```

3. **Start the server**:
   ```bash
   flask --app libraryassembler.app run --debug
   ```

Once running, you can verify the service with the bundled health-check
endpoint:

```bash
curl http://127.0.0.1:5000/api/health
```

The default configuration stores data in `libraryassembler.db`, but you can
override this by setting the `DATABASE_URL` environment variable before running
the application.

### Running tests

The project includes a small test-suite to validate that the Flask factory and
database bootstrap work correctly:

```bash
pytest
```

## Project Structure

As this project is still forming, the structure is evolving. Current ideas include:

- **`src/`**: Where the main code will live, including core functionalities, integration points, and user interface components.
- **`docs/`**: Documentation for developers and users.
- **`tests/`**: A place for unit and integration tests as they are developed.

## Contributing

I need your help to bring LibraryAssembler to life! Whether through code, design, documentation, or simply brainstorming, your contributions are crucial.

Please see the [Contributing Guide](CONTRIBUTING.md) for more details on how to get involved.

## License

This project is licensed under the GPL 3 License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions, ideas, or to get involved, you can reach out by creating an issue or joining the discussion on our GitHub repository.