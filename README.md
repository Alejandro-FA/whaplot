# WhaPlot

A tool for generating cool plots and data visualizations from WhatsApp chats.

## Running the Project

To start the project, simply run the application using the `uv` command. For example:

```shell
uv run whaplot race chat_file.txt
```

Ensure that all dependencies are installed before running the command.

## Code Quality

This project uses `ruff` as a development dependency for linting and formatting.

- To run the linter, execute:

  ```shell
  uv run ruff check --fix
  ```

- To automatically format your code, run:

  ```shell
  uv run ruff format
  ```

- To run the `pyright` type checker, execute:

  ```shell
  uv run pyright
  ```

## Testing

To run the tests, execute:

```shell
uv run pytest
```
