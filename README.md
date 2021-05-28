<br />
<p align="center">
  <a href="https://github.com/naderabdalghani/nfa-elnga7y">
    <img src="assets/icon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">NFA El Nga7y</h3>

  <p align="center">
    A command-line tool that converts a "simple" regular expression into its corresponding nondeterministic finite automaton (NFA) using Thompson’s Construction algorithm
  </p>
</p>

## Table of Contents

* [About the Project](#about-the-project)
  * [Limitations](#limitations)
  * [Sample Run](#sample-run)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Running](#running)

## About The Project

### Limitations

The tool only supports alphanumeric letters for operands and the following regular expression operators written according to their precedence from the highest to the lowest:

1. Grouping `(...)`
2. Duplication `A*`
3. Concatenation `AB`
4. Alternation `A|B`

### Sample Run

Input regex: `10*1(1|0)*`

Output NFA as JSON:

```json
{
    "startingState": "S4",
    "S4": {
        "isTerminatingState": false,
        "1": [
            "S5"
        ]
    },
    "S5": {
        "isTerminatingState": false,
        "Ɛ": [
            "S0"
        ]
    },
    "S0": {
        "isTerminatingState": false,
        "Ɛ": [
            "S1",
            "S3"
        ]
    },
    "S1": {
        "isTerminatingState": false,
        "0": [
            "S2"
        ]
    },
    "S2": {
        "isTerminatingState": false,
        "Ɛ": [
            "S0",
            "S3"
        ]
    },
    "S3": {
        "isTerminatingState": false,
        "Ɛ": [
            "S6"
        ]
    },
    "S6": {
        "isTerminatingState": false,
        "1": [
            "S7"
        ]
    },
    "S7": {
        "isTerminatingState": false,
        "Ɛ": [
            "S14"
        ]
    },
    "S14": {
        "isTerminatingState": false,
        "Ɛ": [
            "S8",
            "S15"
        ]
    },
    "S8": {
        "isTerminatingState": false,
        "Ɛ": [
            "S9",
            "S10"
        ]
    },
    "S9": {
        "isTerminatingState": false,
        "1": [
            "S11"
        ]
    },
    "S10": {
        "isTerminatingState": false,
        "0": [
            "S12"
        ]
    },
    "S11": {
        "isTerminatingState": false,
        "Ɛ": [
            "S13"
        ]
    },
    "S12": {
        "isTerminatingState": false,
        "Ɛ": [
            "S13"
        ]
    },
    "S13": {
        "isTerminatingState": false,
        "Ɛ": [
            "S14",
            "S15"
        ]
    },
    "S15": {
        "isTerminatingState": true
    }
}
```

Output NFA PNG image:

![NFA Graph][nfa-graph]

### Built With

* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Graphviz](https://graphviz.org/)

## Getting Started

### Prerequisites

* Setup Python using this [link](https://realpython.com/installing-python/)
* Setup Graphviz using this [link](https://graphviz.org/download/)
* Make sure you add Graphviz to the system PATH
* Setup the required packages by running `pip install -r requirements.txt`

### Running

* Make sure you are in the project directory:

	`cd <project-directory>`

* Activate the virtual environment, if any:

    - Mac OS or Linux:

        `source venv/bin/activate`

    - Windows:

        `venv\Scripts\activate`

* Finally, run the following line with any regular expression instead of `<regex>`:

	`python main.py "<regex>"`

    - Example:

	    `python main.py "10*1(1|0)*"`

[nfa-graph]: assets/nfa_graph_example.png
