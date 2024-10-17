import sys
import datetime
import colorama
from typing import Optional, Union

colorama.init()

class TextStyle:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printc(
    *args: str,
    sep: str = " ",
    end: str = "\n",
    file: Optional[str] = None,
    flush: bool = False,
    timestamp: bool = False,
    prefix: Optional[str] = None,
    color: Optional[str] = None,
    style: Optional[str] = None,
    **kwargs
) -> None:
    # Prepare the concatenated message
    concatenated_string = sep.join(map(str, args))
    
    # Apply text styles if specified
    if style == 'bold':
        concatenated_string = f"{TextStyle.BOLD}{concatenated_string}{TextStyle.RESET}"
    elif style == 'underline':
        concatenated_string = f"{TextStyle.UNDERLINE}{concatenated_string}{TextStyle.RESET}"
    
    # Add timestamp or prefix if specified
    if timestamp:
        try:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            concatenated_string = f"[{now}] {concatenated_string}"
        except Exception as e:
            print(f"Error formatting timestamp: {e}", file=sys.stderr)
    
    if prefix:
        concatenated_string = f"{prefix}: {concatenated_string}"
    
    # Apply text color if specified
    if color:
        color_code = getattr(colorama.Fore, color.upper(), None)
        if color_code:
            concatenated_string = f"{color_code}{concatenated_string}{colorama.Style.RESET_ALL}"
        else:
            print(f"Invalid color '{color}' specified. Printing without color.", file=sys.stderr)
    
    # Determine where to print
    output_stream = sys.stdout
    if file:
        try:
            output_stream = open(file, 'a')
        except IOError as e:
            print(f"Error opening file '{file}': {e}", file=sys.stderr)
            return
    
    # Print to the appropriate stream
    try:
        print(concatenated_string, end=end, file=output_stream, flush=flush, **kwargs)
    except Exception as e:
        print(f"Error printing: {e}", file=sys.stderr)
    finally:
        if file:
            output_stream.close()

# Example usage
# printc("apple", "banana", "cherry", sep="/", end="***", timestamp=True, color="GREEN")
# 0printc("pineapple", "orange", "grape", sep=", ", file="output.txt", flush=True, prefix="INFO", style="bold")
