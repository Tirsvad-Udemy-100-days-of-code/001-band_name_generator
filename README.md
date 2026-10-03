# 🚀 Band Name Generator

A beginner-friendly Python program that suggests a band name using the user's hometown and pet's name.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)

## 🧭 Overview

This is the Day 1 project from Udemy's [100 Days of Code™: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/). The program asks for the city you grew up in and the name of a pet, then combines them into your band name.

```text
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
Paris
What's the name of a pet?
Rex
Your band name could be: Paris Rex
```

## 📋 Requirements

- Python 3.13 or newer
- No runtime dependencies (the tests use Python's built-in `unittest`)

## 🛠️ Setup

Create a local virtual environment named `.venv` in the project root and activate it.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows (Command Prompt):

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then install the project in editable mode:

```bash
python -m pip install -e .
```

Run `deactivate` to leave the virtual environment. The `.venv` folder is ignored by Git.

## ▶️ Run

With `.venv` active:

```bash
python -m band_name_generator
```

Or use the installed command:

```bash
band-name-generator
```

## 🧪 Tests

With `.venv` active:

```bash
python -m unittest discover -s tests
```

## 📄 License

No license has been chosen yet. Add a `LICENSE` file and name it here once one is picked.

## 🔗 Links

- [Repository](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code)
- [Documentation](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code#readme)
- [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/issues)
