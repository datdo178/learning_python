# VIRTUAL ENVIRONMENT

Refer link:
- https://codelearn.io/sharing/quick-quide-python-virtual-environment
- https://docs.python.org/3/library/venv.html

## 1. Define
- The venv module supports creating lightweight “virtual environments”, each with their own <b>independent set of Python packages installed in their site directories</b>

## 2. Install
- Old python version:<br>
`pip install virtualenv`
<br><br>

- Latest python version: virtualenv is built-in

## 3. Usage
- Create a venv:<br>
`python3 -m venv ./venv`
<br><br>

- Switch to virtual env:<br>
`source ./venv/bin/activate`
<br><br>

- Quit virtual env:<br>
`deactivate`

- Check usage options:<br>
`python -m venv --help`<br>

## 4. Other
- Permanently set PYTHONPATH for virtual env by add export line to ./venv/bin/active:<br>
`export PYTHONPATH=<paths>`