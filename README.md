# Country Explorer

A Python desktop application that retrieves and displays country information using the Countries.dev REST API.

## Features

- Search for countries using their two-letter country codes.
- Display country names, capitals and population.
- Display currency information, including currency codes, names and symbols.
- Display language information and language codes.
- Validate country-code input.
- Handle API request errors.
- Present country information through a Tkinter graphical user interface.
- Store previously searched countries data locally using JSON persistence.
- Reuse cached countries data on subsequent searches.

## Technologies Used

- **Python** — application logic
- **Tkinter** — graphical user interface
- **Requests** — HTTP requests to the REST API
- **JSON** — local data persistence
- **Git and GitHub** — version control and project hosting

## API

Country data is retrieved from the Countries.dev API.

Example endpoint:

`https://countries.dev/alpha/IN`

API documentation: https://countries.dev/docs

## Project Structure

```text
CountryExplorer/
├── Main.py
├── GUI.py
├── Function.py
├── Function_2.py
├── Utils.py
├── Storage.py
├── countries.json
└── README.md
└── LICENSE
```

## Installation and Usage

1. Install Python.
2. Install the Requests library:

   ```bash
   pip install requests
   ```

3. Clone or download this repository.
4. Run the application:

   ```bash
   python Main.py
   ```

5. Enter a two-letter country code, such as `IN`, and search.

## What I Learned

Through this project, I practised:

- Working with REST APIs and HTTP requests.
- Processing JSON responses.
- Organising Python code across multiple modules.
- Handling errors and validating user input.
- Building a desktop GUI with Tkinter.
- Saving and retrieving data using JSON files.
- Integrating API logic, local storage and GUI functionality.

## Future Improvements

- Add a refresh option for cached countries information.
- Improve the presentation of country data.
- Add a comparison feature for multiple countries.

---

**Project:** Country Explorer  
**Status:** Functional learning project

## Author

Anurag Sharma