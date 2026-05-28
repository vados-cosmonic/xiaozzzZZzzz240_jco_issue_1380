just := env_var_or_default("JUST", just_executable())
wac := env_var_or_default("WAC", "wac")
pnpm := env_var_or_default("PNPM", "pnpm")
wasmtime := env_var_or_default("WASMTIME", "wasmtime")

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
    {{just}} --justfile python/justfile build

# Build the C++ component (consumer/importer)
[group('build')]
build-cpp:
    {{just}} --justfile cpp/justfile build

# Build the combined component
[group('build')]
build-combined:
    {{wac}} plug cpp/component.wasm --plug python/component.wasm -o combined.wasm

# Run the combined wasm with wasmtime
[group('run')]
run-wasmtime:
    {{wasmtime}} run combined.wasm

# Run the combined wasm with jco
[group('run')]
run-jco:
    {{pnpm}} -C runner run transpile
    {{pnpm}} -C runner start
