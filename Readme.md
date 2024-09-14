# Cron Expression Parser

## Overview

This a CLI that parses cron expressions and outputs the fields to show at what time the cron is supposed to be executed

## Prerequisites

Make sure Python 3 is installed on your machine.

### Checking Python Version

#### Linux and macOS

Open a terminal and run:

```bash
python --version
```
This should return a python version greater than 3
### Install dependencies using

```bash
pip install -r requirements.txt
```

## Running the Program
unzip the zip provided
Then do the following command format
```bash
cd cronParser/src
python parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

## Tests

The tests in the test folder aren't executing fine because of environment variable issue.
To execute tests add this project to your charm and use the IDE to run tests.