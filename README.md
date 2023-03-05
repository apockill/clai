# clai
Command Line AI- this tool lets you call ChatGPT from a CLI. 

I'm designing this to be used in conjunction with a fork of [shin][shin], which will allow you
to call `clai` from any textbox in your computer. Finally, chatGPT everywhere!

[shin]: https://github.com/apockill/shin
_________________

[![PyPI version](https://badge.fury.io/py/clai.svg)](http://badge.fury.io/py/clai)
[![Test Status](https://github.com/apockill/clai/workflows/Test/badge.svg?branch=main)](https://github.com/apockill/clai/actions?query=workflow%3ATest)
[![Lint Status](https://github.com/apockill/clai/workflows/Lint/badge.svg?branch=main)](https://github.com/apockill/clai/actions?query=workflow%3ALint)
[![codecov](https://codecov.io/gh/apockill/clai/branch/main/graph/badge.svg)](https://codecov.io/gh/apockill/clai)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)
_________________

[Read Latest Documentation](https://apockill.github.io/clai/) - [Browse GitHub Code Repository](https://github.com/apockill/clai/)
_________________

## Installation
1. The recommended installation method is to use `pipx`, via
    ```
    pipx install clai
    ```

1. Then go to [OpenAI] and create an API Key. Once it's generated, add the following to 
   your `.bashrc`:
   ```bash
   export OPENAI_API_TOKEN=<paste here>
   ```

[OpenAI]: https://platform.openai.com/account/api-keys

## Usage
Invoke the assistant with the format `clai <your prompt>`. For example:
```
clai Write an email saying I'll be late to work because I'm working on commandline AIs
```

## Development

### Installing python dependencies
```shell
poetry install
```

### Running Tests
```shell
pytest .
```

### Formatting Code
```shell
bash .github/format.sh
```

### Linting
```shell
bash .github/check_lint.sh
```