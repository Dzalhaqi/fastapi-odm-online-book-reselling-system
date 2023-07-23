<br/>
<p align="center">
  <h3 align="center">
    FastAPI Project
  </h3>

  <p align="center">
    Learn Object Relational Mapping (ODM) by Building Online Book Reselling System Prototype
    <br/>
  </p>
  <p align="center">
    <a href="https://dzalhaqi.github.io/api-docs-fastapi-odm-online-book-reselling-system/">
      View API docs
    </a>
  </p>
</p>

<p align="center">
  <p align="center">
    <img src="https://img.shields.io/github/downloads/dzalhaqi/fastapi-odm-online-book-reselling-system/total"/>
    <img src="https://img.shields.io/github/contributors/dzalhaqi/fastapi-odm-online-book-reselling-system?color=dark-green"/>
    <img src="https://img.shields.io/github/forks/dzalhaqi/fastapi-odm-online-book-reselling-system?style=social"/>
    <img src="https://img.shields.io/github/issues/dzalhaqi/fastapi-odm-online-book-reselling-system"/>
    <img src="https://img.shields.io/github/license/dzalhaqi/fastapi-odm-online-book-reselling-system"/>
  </p>
</p>

## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Description](#description)
  - [Preview API Docs (using Redocly)](#preview-api-docs-using-redocly)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About The Project

### Description
This prototype represents an internet-based repository for books, allowing the submission of pre-owned books for proper cataloging. The books are organized by genre and provided with detailed profiles. Users have the opportunity to buy from this collection of books, and all purchases are accompanied by receipts. To ensure transparency and accountability, all order, payment, and purchasing activities are meticulously recorded for auditing purposes. Overall, this prototype serves as a foundation for the development of an e-commerce platform dedicated to facilitating the exchange and sale of used books with MongoDB as the database storage using Object Relational Mapping technique.

### Preview API Docs (using Redocly)



## Built With

Application deployed is build with **Python** using **FastAPI** library 

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* python

for Windows OS
```sh
python --version 
```

for Unix Based OS (Linux, MacOS, etc)
```sh
python3 --version 
```

* git

```sh
git --version 
```

> note: if you don't have python installed, you can download it [here](https://www.python.org/downloads/) and if you don't have git installed, you can download it [here](https://git-scm.com/downloads)

### Installation

1. Clone the repo

```sh
git clone https://github.com/Dzalhaqi/fastapi-odm-online-book-reselling-system.git
```

2. Create python environment

```sh
python -m venv env
```

3. Activate python environment

* for Windows OS
```sh
env\Scripts\activate
```

* for Unix Based OS (Linux, MacOS, etc)
```sh
source env/bin/activate
```

4. Install python library

```sh
pip install -r requirements.txt
```

5. Run the FastAPI server with uvicorn (default port 8000)

```sh
uvicorn main:app --reload
```

## License

Distributed under the MIT License. See [LICENSE](https://github.com/dzalhaqi/fastapi-odm-online-book-reselling-system/blob/main/LICENSE) for more information.

## Acknowledgements

* [Muhammad Dzalhaqi](https://github.com/dzalhaqi/)
