just := env_var_or_default("JUST", just_executable())

@_default:
    {{just}} --list

# Build the combined component
[group('build')]
build:
    {{just}} build-python
    {{just}} build-cpp
    {{just}} build-combined

# Build the Python component (producer/exporter)
[group('build')]
build-python:
    {{just}} -C python build

# Build the C++ component (consumer/importer)
[group('build')]
build-cpp:
    {{just}} -C cpp build

# Build the combined component
[group('build')]
build-combined:
    {{wac}} plug cpp/component.wasm --plug python/compnent.wasm -o combined.wasm
