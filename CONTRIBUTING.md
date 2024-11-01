# Contributing to Profile and Resume Analyzer

Thank you for your interest in contributing to the Profile and Resume Analyzer! This document will guide you through the setup process, contribution workflow, coding standards, and testing practices. We appreciate your contributions to enhance this project.

---

## Getting Started

### 1. Fork the Repository
   - Click the "Fork" button at the top right of the repository page on GitHub.
   - This will create a copy of the repository under your GitHub account.

### 2. Clone Your Forked Repository
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/<your-username>/profile_resume_analyzer.git
     cd profile_resume_analyzer
     ```

### 3. Create a Branch
   - Create a new branch for your feature or bug fix to keep the main branch stable:
     ```bash
     git checkout -b feature/your-feature-name
     ```

### 4. Set Up Environment Variables
   - Ensure you have a `.env` file in the root directory with the necessary API keys:
     ```plaintext
     LINKEDIN_CLIENT_ID=YOUR_LINKEDIN_CLIENT_ID
     LINKEDIN_CLIENT_SECRET=YOUR_LINKEDIN_CLIENT_SECRET
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY
     ```

### 5. Install Dependencies
   - Set up a virtual environment and install the required packages:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

### 6. Install SpaCy Language Model
   - Download the required English language model for SpaCy:
     ```bash
     python -m spacy download en_core_web_sm
     ```

---

## Contribution Workflow

1. **Make Your Changes**
   - Write clean, well-documented code that follows the project's coding standards.
   - See the **Coding Standards** section for more details.

2. **Write Tests**
   - Ensure you write unit tests for new functionality or bug fixes.
   - We use the `pytest` framework for testing:
     ```bash
     pip install pytest
     pytest
     ```

3. **Check Formatting**
   - Ensure your code follows the PEP 8 style guide. Use `black` for formatting and `flake8` for linting:
     ```bash
     pip install black flake8
     black .
     flake8 .
     ```

4. **Commit Your Changes**
   - Use clear, descriptive commit messages to describe your changes.
     ```bash
     git add .
     git commit -m "Add feature: automated resume analysis"
     ```

5. **Push Your Branch**
   - Push your changes to your forked repository:
     ```bash
     git push origin feature/your-feature-name
     ```

6. **Create a Pull Request (PR)**
   - Go to the original repository on GitHub and create a PR from your branch.
   - Provide a detailed description of your changes and why they are needed.

---

## Coding Standards

- **Python Style**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for consistent code style.
- **Docstrings**: Include clear and concise docstrings for all functions and classes using the Google docstring style.
- **Comments**: Add comments for complex logic or workflows in your code.
- **Commit Messages**: Use descriptive, concise messages (e.g., "Fix LinkedIn API authentication error").
- **Modularization**: Keep related code organized in functions or classes and avoid duplicating code.

---

## Testing Guidelines

Testing is crucial to ensure that the application works as expected. Here are some guidelines for effective testing:

- **Unit Tests**: Write tests for any new functionality, especially if it involves complex logic.
- **Functional Tests**: Test the full application flow, especially for critical user interactions.
- **Run All Tests Before Submitting**: Make sure all tests pass before creating a PR.
  ```bash
  pytest
  ```

---

## Additional Resources

- **Documentation**: Review `README.md` and code docstrings to understand the project structure.
- **Questions**: If you have any questions, please open an issue or reach out to the maintainers.

Thank you for contributing to this project! Your efforts help make the Profile and Resume Analyzer more effective and valuable for users.
