# Library Assembler - PLANNING.md

#### **Project Vision**
LibraryAssembler aims to be a modern and comprehensive digital library organizer for various types of media, including eBooks, audiobooks, comics, magazines, and more. The project takes inspiration from management tools like Sonarr and Radarr, emphasizing automation, metadata enrichment, and a user-friendly interface.

---

## **Project Roadmap**
The following tasks and milestones are organized into technical (Engineering), design (UI/UX), and documentation deliverables:

---

### **Phase 1: Foundational Setup**
**Timeline: 2-3 Weeks**

1. **Technical (Engineer)**
    - Finalize application architecture.
        - Define technology stack (Python Flask/Microservices for backend, React.js or equivalent for frontend, etc.).
        - Establish database schema structure for metadata, library collections, and user settings.
    - Implement and test initial API routes:
        - User authentication and session management.
        - Health check endpoint verification (`/api/health` as a POC is already implemented but expand to encompass more status checks).
        - Basic CRUD operations for user accounts, library items, and metadata input.
    - Establish CI/CD pipelines using GitHub Actions:
        - Linting, testing, and code coverage integration.
        - Deploy to a sandbox/cloud environment.

2. **Design (Designer)**
    - Create basic wireframes for:
        - Library dashboard (user-friendly UI to access, search, and view collections).
        - Content detail pages for individual eBooks, audiobooks, or comics.
        - User settings/preferences and metadata management interface flows.

3. **Documentation (Writer)**
    - Draft the **Project Architecture Document**:
        - High-level description of the backend (Flask) and how it integrates with API.
        - Explanation of the database schema and relationships.
    - Write **Setup and Contribution Guide** to support new contributors, covering:
        - Project structure overview (referencing ideas from `README.md` and improving them).
        - Clear instructions on setting up a local development environment.
    - Draft initial **User Guide** with instructions on project installation, server setup, and initial use case.

---

### **Phase 2: Metadata Management and Organization Automation**
**Timeline: 4-6 Weeks**

1. **Technical (Engineer)**
    - Design and develop a metadata fetching system:
        - Integrate with common APIs/databases (e.g., Amazon, Audible, Goodreads, OpenLibrary, Google Books) for metadata retrieval.
        - Create API endpoints to search, fetch, and update metadata.
    - Build basic library organization features:
        - Support folder/file monitoring for content and sync updates to the library.
        - Implement rules for categorizing into genres, authors, series, and tags.
        - Establish logging for debugging organization issues.
        
2. **Design (Designer)**
    - Develop a clickable prototype for user feedback, focusing on:
        - The library interface for viewing, searching, and managing files.
        - The streamlined metadata display (title, author, cover image, series) on card-based layouts.
        - Intuitive configurations for automatic sorting rules and metadata fetching setups.

3. **Documentation (Writer)**
    - Document required metadata fields based on supported APIs (category, title, author, tags, date published, etc.).
    - Detail API design specifications, including request/response examples for:
        - Retrieving metadata for a single file or batch of files.
        - Searching and selecting metadata from external API sources.
        - Managing user-specific metadata (preferences, custom tags, etc.).

---

### **Phase 3: Advanced Features & Enhanced User Experience**
**Timeline: 8-12 Weeks**

1. **Technical (Engineer)**
    - Implement advanced features like:
        - Bulk editing of metadata.
        - Synchronization with cloud storage (e.g., Google Drive, Dropbox).
        - Advanced custom tagging and filtering options within the library.
    - Implement pagination and search functionality for large libraries.
    - Begin integrating third-party libraries for eBook, audiobook, and comic file previews:
        - E.g., embedded PDF/ePub readers, audio players, comic viewer.

2. **Design (Designer)**
    - Finalize a responsive web interface.
    - Design user onboarding experience (covering setup, connecting library, and customization).

3. **Documentation (Writer)**
    - Build detailed tutorials for cloud storage synchronization and third-party API configuration (e.g., OpenLibrary, Goodreads login).
    - Write API endpoint usage examples.
    - Prepare documentation on how advanced features (e.g., tagging) work.
---

#### Specific Task Assignments

**Writer:**
- Project Architecture Document (overview of backend and database schema).
- Documentation for contributor onboarding, including local development setup.
- User Guide with installation and setup steps.
- API documentation for current and planned features.
- Guides for setting up integrations (metadata APIs, cloud storage).

**Designer:**
- Dashboard wireframes showcasing file sorting results and search interface.
- Library browse and organization UI (including cards, tags, categories).
- Settings UI for metadata and library sync control.
- Preparation of interactive mockups for feedback loops with stakeholders.

**Engineer:**
- Expand Flask app:
    - User authentication and session handling.
    - Database schema setup (`books`, `audiobooks`, `tags`, `collections`, `users` tables).
    - Metadata fetching and API integration (OpenLibrary, Goodreads, etc.).
    - Core library organization logic (ingestion, categorization, logging).
    - Implement basic backend tests for each service.

- Implement CI/CD pipelines for rapid integration.
- Improve application error handling/logging mechanisms.

---

#### MVP Release Scope
LibraryAssembler's MVP (Minimum Viable Product) should emphasize:
1. Intuitive library ingestion and organization for key media types (eBooks, Comics, Audiobooks).
2. Metadata fetching with configurable tagging rules.
3. A basic web-based UI offering a library dashboard, search functionalities, and a content detail view.
4. Integrated test coverage and CI/CD pipelines supporting contributors in expanding the features.
