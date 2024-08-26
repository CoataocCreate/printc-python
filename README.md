# `printc`: Enhanced Print Function for Python

`printc` is an advanced Python package that extends the built-in `print` function. It introduces additional features such as timestamping, text styling, colored output, and file logging, offering greater flexibility and customization options for your print statements.

## Features

- **Timestamps**: Add timestamps to your messages to track when they were logged.
- **Prefixes**: Easily add customizable prefixes to messages for improved categorization.
- **Text Styling**: Apply text styles like bold and underline to enhance readability.
- **Text Coloring**: Print text in various colors (requires `colorama` package) for better visual differentiation.
- **File Output**: Redirect output to files for logging purposes, in addition to standard output and error streams.
- **Flexible Parameters**: Customize output behavior with parameters such as `sep`, `end`, and `flush`.
- **Robust Error Handling**: Gracefully handle errors related to timestamp formatting, file operations, and general printing.

## Installation

To install `printc`, use pip:

```bash
pip install printc
```

## Usage

Here are some examples demonstrating how to use `printc` with its various features:

```python
from printc import printc

# Basic Usage
printc("Hello", "World", sep="-", end="!\n")

# Adding Timestamps
printc("Logging message", timestamp=True)

# Adding Prefixes
printc("File not found", prefix="ERROR")

# Styling Text
printc("Bold text", style="bold")
printc("Underlined text", style="underline")

# Coloring Text (requires colorama package)
printc("Red text", color="RED")
printc("Blue text", color="BLUE")

# Output to a File
printc("Log entry", file="output.log")

# Customized Usage with All Options
printc(
    "Detailed log entry",
    timestamp=True,
    prefix="INFO",
    style="bold",
    color="GREEN",
    file="output.log",
    flush=True
)
```

## Parameters

- **`*args`**: Variable-length arguments to print.
- **`sep`**: Separator between arguments (default is `" "`).
- **`end`**: Ending character(s) at the end of the printed line (default is `"\n"`).
- **`file`**: Output stream; `None` for standard output or specify a file path for file output.
- **`flush`**: Whether to flush the output stream (default is `False`).
- **`timestamp`**: Whether to prepend messages with timestamps (default is `False`).
- **`prefix`**: Prefix string for messages (default is `None`).
- **`color`**: Text color (requires `colorama` package).
- **`style`**: Text style (`bold`, `underline`, or `None` for normal text).
- **`**kwargs`**: Additional keyword arguments passed to the underlying `print` function.

## Dependencies

- **`colorama`**: Required for text coloring. This package is automatically installed with `printc`.

## Acknowledgments

- Inspired by the need for more advanced printing capabilities in Python applications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you’d like to contribute to `printc`, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure that your code adheres to the project's coding style and includes appropriate tests.

```

Feel free to adjust any sections as needed!
