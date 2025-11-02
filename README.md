# Assignment 5 for UCLA-CS35L

## How to setup 
To set up the project using pipenv:

1. **Install pipenv** (if you don't already have it):
   ```
   pip install pipenv
   ```

2. **Install dependencies**:
   ```
   pipenv install
   ```

3. **Activate the virtual environment**:
   ```
   pipenv shell
   ```

Now you are ready to run the project Python files inside the pipenv environment!

## Installation and Usage

### Install the project in editable mode

You can install the project in editable (`-e`) mode using pipenv. First, make sure you are in the project root directory (where `pyproject.toml` is located) and you have activated the pipenv shell (as described in the setup section above):

```
pipenv install -e .
```

Alternatively, if you're not in the pipenv shell, you can use:

```
pipenv run pip install -e .
```

### Running the main program

After installation, you can run the program in several ways:

#### Using the `user-profiles` command directly

Once installed, you can use the `user-profiles` command directly (inside the pipenv shell):

**Example 1: Sort by age and output to a file**
```
user-profiles --input input.json --output sorted_by_age.json --sort age
```

**Example 2: Sort by name and output to the screen (stdout)**
```
user-profiles --input input.json --sort name
```

If you're not in the pipenv shell, you can use:
```
pipenv run user-profiles --input input.json --output sorted_by_age.json --sort age
```

#### Using Python module syntax

Alternatively, you can execute the main script using the `-m` flag with Python. If you're inside the pipenv shell (activated with `pipenv shell`), you can run:

**Example 1: Sort by age and output to a file**
```
python -m app.main --input input.json --output sorted_by_age.json --sort age
```

**Example 2: Sort by name and output to the screen (stdout)**
```
python -m app.main --input input.json --sort name
```

Alternatively, if you're not in the pipenv shell, you can use `pipenv run`:

```
pipenv run python -m app.main --input input.json --output sorted_by_age.json --sort age
```

Replace `input.json` with the path to your input file. The `--sort` flag can be set to `age`, `name`, `email`, or `location`.

