# LinkedIn Profile Analyzer

The LinkedIn Profile Analyzer is a Python application that analyzes your LinkedIn profile and provides suggestions for improvement. It uses the LinkedIn API to extract relevant information from your profile, and the Spacy library to analyze the text and identify areas for improvement. The application is designed to be run in a web browser using the Streamlit library. It uses NLP for natural language processing and analysis, and its powered by the OpenAI API for summarization and recommendations.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Forks](https://img.shields.io/github/forks/hipnologo/linkedIn_profile_analyzer)](https://github.com/hipnologo/linkedIn_profile_analyzer/network/members)
[![Stars](https://img.shields.io/github/stars/hipnologo/linkedIn_profile_analyzer)](https://github.com/hipnologo/linkedIn_profile_analyzer/stargazers)
[![Issues](https://img.shields.io/github/issues/hipnologo/linkedIn_profile_analyzer)](https://github.com/hipnologo/linkedIn_profile_analyzer/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/hipnologo/linkedIn_profile_analyzer)](https://github.com/hipnologo/linkedIn_profile_analyzer/graphs/contributors)

## Installation

To run the LinkedIn Profile Analyzer, you will need to install the following libraries:

- `streamlit`
- `linkedin-api`
- `spacy`
- `en_core_web_sm`
- `openai`

You can install these libraries using the following command:

``` 
pip install streamlit linkedin-api spacy
python -m spacy download en_core_web_sm
```


You will also need to set up a LinkedIn Developer account and obtain API credentials. You can do this by following the instructions on the [LinkedIn Developer Platform website](https://www.linkedin.com/developers/).

## Usage

To run the LinkedIn Profile Analyzer, navigate to the directory where the code is stored and enter the following command in your terminal:

```
streamlit run linkedin_analyzer.py
```
Note: OPENAI_API_KEY will be needed in order to use the ChatGPT API.

This will launch the Streamlit interface in your web browser. Enter your LinkedIn profile URL and click "Analyze" to view the analysis and suggestions.

## Contributing

We welcome contributions to this project! If you have an idea for a feature or bug fix, follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes to the new branch.
4. Push the branch to your forked repository.
5. Submit a pull request to the original repository.

Make sure to follow the code style and add test cases for any new code. If you have any questions, don't hesitate to ask the repository maintainers.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

The LinkedIn Profile Analyzer is licensed under the MIT license. See `LICENSE` for details.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Fabio Carvalho - [@fabioac](https://twitter.com/fabioac)

Project Link: [https://github.com/hipnologo/linkedIn_profile_analyzer](https://github.com/hipnologo/linkedIn_profile_analyzer)

<p align="right">(<a href="#top">back to top</a>)</p>

<a href="https://www.buymeacoffee.com/hipnologod" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
