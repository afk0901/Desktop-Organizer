

# 🧹 Desktop Organizer – Python Automation Tool

Tired of your cluttered Desktop?

This is a small Python script that cleans up your Windows Desktop by sorting files into folders by extension. PDFs go with PDFs, Word docs with Word docs, and so on by running one command.

Run it once and everything is where you expect it to be!

## 🔹 Highlights
- Built in pure Python
- Packaged as `.exe` (runs without Python installed)
- Uses Windows Registry to detect Desktop (OneDrive-safe)
- Fully tested with 27 Pytest test cases
- Designed for extensibility and safety

## Current Features

Automatically sorts:
  - `.pdf` → `PDF Documents`
  - `.docx`, `.doc` → `Word Documents`
  - `.xlsx`, `.xls`, `.odt` → `Excel Documents`
  - `.txt` → `Text Documents`
- Resolves correct Desktop path (supports OneDrive and standard setups)
- Packaged as .exe – no Python needed for users

## How to install the project's dependencies

Run this command in the terminal: `pip install -r ./requirements.txt` and 
that should be it.

## How to run the tool

Download the .exe from the latest release in this repository or clone the repo and follow the instructions below.

The main entry file is desktop_organizer.py. Run it in your IDE or run this command inside the root directory of the project: 
`python desktop_organizer.py`. This command should start the tool.

## 🧪 Tests

This project includes automated tests to verify file movement behavior and handling edge cases.

The project uses Pytest for all it's tests. You can run the tests in your IDE or run them all manually in the 
terminal by simply writing `python -m pytest` in the terminal in the root of the project and hit enter.

