## Log File Metrics

This script reads log files from standard input, computes metrics on the file size and status codes, and outputs the metrics after every 10 lines of input or when a keyboard interruption occurs. The log file format must be:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

If the input line does not match this format, it will be skipped.

### Usage

To use the script, pipe the log file into the script via standard input. For example, if the log file is called access.log, you can run the script as follows:

```
$ cat access.log | python3 log_metrics.py
```

The script will then output the total file size and the number of lines by status code every 10 lines of input or when a keyboard interruption occurs.

### Output
The script outputs the following metrics:

Total file size: the sum of all previous file sizes in the log file.
Number of lines by status code: a count of the number of lines in the log file with each status code. Only the following status codes are counted: 200, 301, 400, 401, 403, 404, 405, and 500.
The output is printed to standard output after every 10 lines of input or when a keyboard interruption occurs.

### Implementation
The script is implemented in Python 3 and uses a dictionary to keep track of the count of lines with each status code. It catches any exceptions that occur while reading input and skips lines that do not match the log file format.

The script can be easily modified to adjust the output format or to handle different log file formats.

Author
This script was written by [Nyamani Matiko].