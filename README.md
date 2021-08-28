# DevOps course project

Project to be used during the course.

## Description

Simple app displaying current time in MSK.

## Getting Started

### Installing

Clone the repository
`git clone https://github.com/TAPAKAH20/devops.git`

#### Python

Install requirements

```Bash
cd devops/python_app
pip3 install -r requirements.txt
```

#### Docker

``` Bash
docker pull r0ach20/devops
```

### Unit Tests

Testing is performed via standart python test framework `unittest`

```Bash
python3 python_app/tests.py
```

### Executing program

#### Python version

``` Bash
cd devops/python_app
export FLASK_APP=main
flask run
```

#### Docker container

``` Bash
docker run r0ach20/devops -p 5000:5000
```

## Version History

* 0.14
  * Unit tests
* 0.13
  * Practices update
* 0.12
  * Docker, REAMDE update
* 0.11
  * Markdown files added
* 0.10
  * Initial Release

## Acknowledgments

Inspiration, code snippets, etc.

* [Simple readme template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
