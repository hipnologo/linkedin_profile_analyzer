# Profile and Resume Analyzer

The Profile and Resume Analyzer is a Python application that uses natural language processing (NLP) to analyze LinkedIn profiles and resumes, providing insights and suggestions for improvement. The application is built with Streamlit for an intuitive web interface, utilizes the LinkedIn API for profile data extraction, and leverages OpenAI's API for generating summaries and recommendations.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Forks](https://img.shields.io/github/forks/hipnologo/profile_resume_analyzer)](https://github.com/hipnologo/profile_resume_analyzer/network/members)
[![Stars](https://img.shields.io/github/stars/hipnologo/profile_resume_analyzer)](https://github.com/hipnologo/profile_resume_analyzer/stargazers)
[![Issues](https://img.shields.io/github/issues/hipnologo/profile_resume_analyzer)](https://github.com/hipnologo/profile_resume_analyzer/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/hipnologo/profile_resume_analyzer)](https://github.com/hipnologo/profile_resume_analyzer/graphs/contributors)

## Features

- **LinkedIn Profile Analysis**: Uses LinkedIn API to fetch profile data and NLP to analyze key sections for improvements.
- **Resume Analysis**: Allows users to upload a PDF of their resume for text extraction and analysis.
- **Automated Suggestions**: Provides recommendations on areas for improvement in both LinkedIn profiles and resumes using NLP and pattern matching.
- **Summarization & Recommendations**: Utilizes OpenAI’s API to generate a summary and specific recommendations for improvement.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/hipnologo/profile_resume_analyzer.git
   cd profile_resume_analyzer
   ```

2. **Set Up Environment Variables**
   - Create a `.env` file in the root directory and add the required API keys:
     ```plaintext
     LINKEDIN_CLIENT_ID=YOUR_LINKEDIN_CLIENT_ID
     LINKEDIN_CLIENT_SECRET=YOUR_LINKEDIN_CLIENT_SECRET
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY
     ```

3. **Install Dependencies**
   - Install the required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Install SpaCy Language Model**
   - Download the English language model for SpaCy:
     ```bash
     python -m spacy download en_core_web_sm
     ```

## Usage

To start the Profile and Resume Analyzer, navigate to the project directory and run the following command:

```bash
streamlit run app.py
```

This will launch the Streamlit interface in your web browser. Enter your LinkedIn profile URL or upload a resume in PDF format to view an analysis and receive suggestions for improvement.

> **Note**: Ensure that you have your `OPENAI_API_KEY` and LinkedIn API credentials set up in the `.env` file.

## Contributing

We welcome contributions to the Profile and Resume Analyzer! To contribute:

1. **Fork the repository** on GitHub.
2. **Clone your fork**:
   ```bash
   git clone https://github.com/<your-username>/profile_resume_analyzer.git
   ```
3. **Create a branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and ensure they meet project guidelines (see [CONTRIBUTING.md](CONTRIBUTING.md)).
5. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a pull request** to merge your changes into the main repository.

For more detailed instructions, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

The Profile and Resume Analyzer is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

Fabio Carvalho - [@fabioac](https://twitter.com/fabioac)

Project Link: [https://github.com/hipnologo/profile_resume_analyzer](https://github.com/hipnologo/profile_resume_analyzer)

<a href="https://www.buymeacoffee.com/hipnologod" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

---

<p align="right">(<a href="#top">back to top</a>)</p>
```

### Summary of Updates

- **Features Section**: Outlined key features for clarity.
- **Installation & Usage**: Detailed steps for setting up and running the app, including the `.env` configuration.
- **Contributing**: Linked to the `CONTRIBUTING.md` for more comprehensive contribution guidelines.
- **License & Contact**: Provided information on licensing and contact details for easy reference. 

This **README.md** provides clear guidance for users and contributors, streamlining both usage and collaboration.