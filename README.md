

<div align="center">
  Yearning2XLSX
  <br />

  <br />
  <a href="https://github.com/lc5900/yearning2xlsx/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/lc5900/yearning2xlsx/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/lc5900/yearning2xlsx/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/lc5900/yearning2xlsx.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/lc5900/yearning2xlsx/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by lc5900](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-lc5900-ff1414.svg?style=flat-square)](https://github.com/lc5900)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
- [Project assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [License](#license)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

This Python script is designed to export query results from Yearning, a database auditing platform, into an XLSX format file. The motivation behind creating this script stems from the limitations of Yearning's native export feature, which outputs results in CSV format that often leads to messy and inconvenient formatting issues.



## Getting Started

### Prerequisites

- Python 3.x
- Dependencies: Before running the script, make sure to install the necessary Python dependencies listed in the `requirements.txt` file.

### Installation

1. Clone the repository to your local machine or download the ZIP file and extract it.
2. Navigate to the script's directory in your terminal or command prompt.
3. Install the required dependencies by running the following command:

## Usage

To use the script, follow these steps:
1. Open the browser and go to the Network tab in Developer Tools (usually activated by pressing F12).
2. Execute your query in Yearning and find the corresponding query request in the Network tab.
3. Copy the entire JSON response body (including the outermost curly braces) from the request's response.
4. Paste the JSON into a text file and save it.
5. In the terminal or command prompt, navigate to the directory where the Python script is located.
6. Run the script using the following command, replacing `path_to_file.txt` with the path to your text file containing the JSON:
python main.py path_to_file.txt
For example, if your text file is named `test.txt` and is located in the same directory as the script, use the following command:
python main.py test.txt
The script will generate an XLSX file with the same name as the text file in the current directory.

## Roadmap

See the [open issues](https://github.com/lc5900/yearning2xlsx/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/lc5900/yearning2xlsx/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/lc5900/yearning2xlsx/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/lc5900/yearning2xlsx/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support


Reach out to the maintainer at one of the following places:

- [GitHub issues](https://github.com/lc5900/yearning2xlsx/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
- Contact options listed on [this GitHub profile](https://github.com/lc5900)

## Project assistance

If you want to say **thank you** or/and support active development of Yearning2XLSX:

- Add a [GitHub Star](https://github.com/lc5900/yearning2xlsx) to the project.
- Tweet about the Yearning2XLSX.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make Yearning2XLSX **better**!

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.


Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [lc5900](https://github.com/lc5900).

For a full list of all authors and contributors, see [the contributors page](https://github.com/lc5900/yearning2xlsx/contributors).

## Security

Yearning2XLSX follows good practices of security, but 100% security cannot be assured.
Yearning2XLSX is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.

