# DevOps course project

Project to be used during the course.

## Description

Simple app displaying current time in MSK.

## Getting Started

### Built with

* Flask 1.1.4+
* Python 3.6.9+

#### Linters

* [Pylint](https://www.pylint.org/)
* [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli)
* [Haskell Dockerfile Linter](https://github.com/hadolint/hadolint)

### Installing

Clone the repository
`git clone https://github.com/TAPAKAH20/devops_pjct.git`

Install flask
`pip3 install flask`

### Executing program

Python version

``` Bash
cd devops_pjct/python_app
flask run
```

Docker container

``` Bash
docker pull r0ach20/devops
docker run r0ach20/devops -p 5000:5000
```

## Version History

* 0.12
    * Docker, REAMDE update
* 0.11
    * Markdown files added
* 0.10
    * Initial Release

## Acknowledgments

Inspiration, code snippets, etc.

* [Simple readme template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
