# 2016-09-12-pipeline-demo
Demonstration of application design using pipeline processing (generators, coroutines, iteration, functional)

# Installation

1. Setup a virtual environment for the project.
2. Activate the virtual environment.
3. Install project requirements via PIP.
  3.1 pip install -r /path/to/2016-09-12-pipeline-demo/requirements.txt

# Summary

This project will demonstrate how python applications can be designed as adaptable pipeline processors.

# Inputs

An input component is a generator object which lazily consumes string input. Each time a newline is encountered,
the generator must split the string at each whitespace, turning the string into an list of strings and yield
the list back to the iterating caller.

# Filters

A filter component is a generator which accepts a list of strings via the send() method. The filter must
yield the original list of strings to the caller if no filtering is needed, and None when filtering is required.

# Transformers

A transformer component is a generator which accepts a list of strings via the send() method. The transformer
must return a modified list of strings to the caller.

# Outputs

An output component is a generator which accepts a list of strings via the send() method. The output must
combine the list by a whitespace and send them to the destination.
