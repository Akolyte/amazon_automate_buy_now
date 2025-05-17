# LinkedIn Job Search Automation

This python script when run will automatically open LinkedIn to a job search based on these criteria:

- **Job Title**
- **Location**
- **Salary**

This way you can apply for all the listed jobs, cross them out using the LinkedIn UI, and then in another 10 minutes (the default amount of time to wait) the tool will check if there are any more jobs. If there are, chrome will automaticlaly open to the query page, and if not then chrome will remain closed and you can go about your day without having to constantly refresh the page for new jobs.

## Prerequisites

1. You need to have Google Chrome installed on your system. The script uses Chrome for browser automation, so make sure it is available in your system's PATH. If you don't have Chrome, download it from [here](https://www.google.com/chrome/).

2. Make sure you have [uv](https://github.com/astral-sh/uv) installed. If you don't have it yet, you can install it with:

```bash
pip install uv
```

## Installation

To install this project using [uv](https://github.com/astral-sh/uv):

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

## Configurable Parameters

The following constants can be configured in `main.py` to customize your job search:

- **JOB_TITLE** (`str`): The job title to search for (e.g., `"Machine Learning Engineer"`).
- **NUMBER_OF_SECONDS_TO_WAIT** (`int`): Base number of seconds to wait between operations (e.g., `600`).
- **LOCATION_ID** (`str`): Location identifier (e.g., `"90000070"` for "United States").
- **SALARY** (`int`): Target salary value (e.g., `120000`).

Adjust these constants in `main.py` as needed to tailor the automation to your preferences.
