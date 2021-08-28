# PYHTON.md


Flask is easy to start and relatively lightweight framework, and i had a
minor amount of expierence with it.

For unit testing `unittest` is used.

## Python best practices found

1. Creating `requirements.txt` file
2. Using a linter
3. Creating function documentation
4. PEP8 style
5. Correcting broken code immediately
6. Using virtual environments
7. Code repo and version control
8. Python Zen
9. Object-oriented approach
10. Write readable code

## Flask specific best practises

1. Breaking project into simple packages
2. Using app factories and `current_app` function
3. Extracting configuration into separate .yaml files
4. Use `celery` for task queue

## Unit testing best practices
1. Tests should be fast
2. Tests should be simple
4. Tests should be readable
5. Tests should be deterministic
6. Unit tests could be run in isolation
7. The test should be able to automatically detect if it passed
8. Use long and descriptive names for testing functions.

### Linters used

* [Pylint](https://www.pylint.org/) for python
* [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) for markdown
* [Haskell Dockerfile Linter](https://github.com/hadolint/hadolint) for Dockerfile
