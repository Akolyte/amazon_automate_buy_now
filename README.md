# LinkedIn Job Search Automation

This python script when run will automatically open LinkedIn to a job search based with these configurable parameters:

## Prerequisites

Make sure you have [uv](https://github.com/astral-sh/uv) installed. If you don't have it yet, you can install it with:

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
