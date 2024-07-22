# python-time-handling

## Description
This Python script demonstrates various time-related functionalities, including fetching the current time, formatting time, and searching for files in the directory structure.

## Installation
To run this project, you'll need to have Python installed.

## Usage
Run the script using the following command:
```sh
python time_script.py
```

## Code Explanation
This script performs the following tasks:

- Imports the `time`, `datetime`, and `os` libraries.
- Fetches the current time in seconds since the epoch and prints it.
- Converts the fetched time into a datetime object and prints it.
- Gets and prints the local time as a string.
- Prints the current UTC time.
- Fetches and prints the current local time as a tuple.
- Formats and prints the current local time as a string.
- Prints several lines with time delays between them.
- Prompts the user to enter a file name and searches for it starting from the current directory and its subdirectories.
- Prints the location of the file if found, or a message indicating that the file was not found.

## Error Handling
The script includes basic error handling for file searching to ensure it works in different directory structures.

## License
This project is licensed under the MIT License
