# URL Shortener

An efficient URL shortener application built with Flask, MongoDB, and basic HTML/CSS. This project provides functionality to shorten URLs and redirect users using shortened links, with a simple front-end for user interaction.

## Features

- Shorten URLs and store them in a MongoDB database
- Redirection from shortened URLs to original URLs
- Basic HTML/CSS front-end interface

## Project Structure
url-shortener/
├── app/
│   ├── __init__.py         # Initializes the Flask app and database connection
│   ├── models.py           # Defines database models (e.g., URL)
│   ├── routes.py           # Defines all routes for shortening and redirecting URLs
│   ├── utils.py            # Contains URL shortening logic and helper functions
│   └── templates/
│       ├── base.html       # Base HTML template
│       └── index.html      # Form for URL input and shortened URL output
├── static/
│   └── style.css           # Basic styling for the front-end
├── config.py               # Configuration for Flask and MongoDB
├── LICENSE                 # MIT License
├── README.md               # Project documentation
└── run.py                  # Entry point to run the Flask app


## Tech Stack

- **Backend**: Flask
- **Database**: MongoDB
- **Front-end**: HTML, CSS

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/chipateni/url-shortener.git
    cd url-shortener
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure MongoDB in `config.py`.

4. Run the application:

    ```bash
    python run.py
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
