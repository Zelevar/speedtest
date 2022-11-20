# Speedtest
Simple script to test internet speed using `speedtest-cli` module

# Usage
Install the `speedtest-cli` module:
`pip install speedtest-cli`

Run the script and wait:
`python main.py`

# Notes
 - Don't name the script `speedtest.py` to avoid an ImportError exception
 - Make sure you don't have third-party interfering modules installed:
 `pip uninstall speedtest`
 - Use secure mode to avoid getting a **403: Forbidden** error
