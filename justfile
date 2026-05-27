just := env_var_or_default("JUST", just_executable())

@_default:
    {{just}} --list

build-python:
    {{just}} -C python build
