# Contributing to LibraryAssembler

Thank you for your interest in contributing to LibraryAssembler! As the sole creator of this project, I'm excited to collaborate with others to build something truly special. This document outlines how you can get involved, whether you're reporting bugs, suggesting new features, or contributing code.

## Table of Contents

- [Contributing to LibraryAssembler](#contributing-to-libraryassembler)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [How Can I Contribute?](#how-can-i-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Features](#suggesting-features)
    - [Contributing Code](#contributing-code)
    - [Improving Documentation](#improving-documentation)
  - [Development Workflow](#development-workflow)
    - [Setting Up Your Environment](#setting-up-your-environment)
    - [Branching Strategy](#branching-strategy)
    - [Making Changes](#making-changes)
    - [Commit Guidelines](#commit-guidelines)
    - [Pull Request Process](#pull-request-process)
  - [License](#license)

## Code of Conduct

To ensure a positive environment for all contributors, please adhere to the (TBD) [Code of Conduct](CODE_OF_CONDUCT.md). This will help maintain a welcoming and collaborative atmosphere.

## How Can I Contribute?

### Reporting Bugs

If you encounter any bugs, your reports would be invaluable. Before submitting a report, please check the [issue tracker](https://github.com/crow50/libraryassembler/issues) to see if it has already been noted.

- **Create a Bug Report**: [Submit a new bug report](https://github.com/crow50/libraryassembler/issues/new?template=issue_template.md) with a clear and descriptive title. Please include as much detail as possible, such as steps to reproduce the issue, expected behavior, and screenshots if applicable.

### Suggesting Features

If you have ideas for new features, I’d love to hear them! Before suggesting something new, please check the [existing feature requests](https://github.com/crow50/libraryassembler/issues?q=is%3Aissue+is%3Aopen+label%3A%22feature+request%22) to see if your idea has already been proposed.

- **Submit a Feature Request**: [Propose a new feature](https://github.com/crow50/libraryassembler/issues/new?template=issue_template.md) with a clear and descriptive title. Provide details on what the feature should do, its benefits, and any potential challenges.

### Contributing Code

I'm excited to accept code contributions! Here's how you can get started:

1. **Fork the Repository**: Fork the project on GitHub and clone your fork locally.
2. **Create a Branch**: Use a descriptive name for your branch (e.g., `feature/metadata-retrieval`, `bugfix/ui-glitch`).
3. **Make Your Changes**: Implement your changes, following the coding standards outlined below.
4. **Commit Your Changes**: Follow the commit guidelines described in the [Commit Guidelines](#commit-guidelines) section.
5. **Submit a Pull Request**: Push your branch to your fork and open a pull request against the `main` branch of the original repository. Provide a clear and descriptive title and description for your pull request.

### Improving Documentation

Good documentation is crucial, and your help in improving it is greatly appreciated. You can contribute by:

- Enhancing the existing documentation in the `docs/` directory.
- Adding new documentation for features, setup guides, or API references.
- Correcting typos, improving clarity, or providing better examples.

## Development Workflow

### Setting Up Your Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/crow50/libraryassembler.git
   cd libraryassembler
   ```

2. **Install Dependencies**:
   - Follow the instructions in the `README.md` to install any required dependencies and set up your development environment.

### Branching Strategy

Here's how I manage the branches:

- **`main` branch**: Contains the stable, released code.
- **`dev` branch**: Used for active development. Features and fixes should be merged here first.
- **Feature branches**: Create feature branches from `dev` for new features (`feature/feature-name`).
- **Bugfix branches**: Create bugfix branches from `dev` for fixing bugs (`bugfix/bug-name`).

### Making Changes

- Ensure your code adheres to the existing coding style.
- Add or update tests as necessary.
- Run the tests to make sure nothing is broken.

### Commit Guidelines

- **Commit Messages**: Please write clear and concise commit messages. Start each message with a capitalized verb (e.g., "Fix", "Add", "Update").
- **Multiple Commits**: If your changes are substantial, consider breaking them into smaller, logical commits.

Example commit message:
```
Fix metadata retrieval issue for books without ISBN

- Added fallback mechanism for books missing ISBN
- Updated tests to cover this case
```

### Pull Request Process

- **Describe Your Changes**: Clearly explain what your pull request does and why it's needed.
- **Link to Issues**: If your PR addresses an issue, please link to it in the description.
- **Review Process**: I will review your pull request. There might be some back-and-forth discussion or changes needed before it gets merged.
- **Stay Involved**: Please be ready to respond to any questions or feedback on your pull request.

## License

By contributing to LibraryAssembler, you agree that your contributions will be licensed under the GPL 3 license.