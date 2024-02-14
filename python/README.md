# bos-api-demo

Welcome to the `bos-api-demo` project! This guide aims to make setup and usage as straightforward as possible, even if you're relatively new to Python, Poetry, gRPC, or any other technologies we use here.

## Installation

Before diving in, let's ensure you've got everything you need.

### Prerequisites

To get started with this project, you will need:

- **Python 3.8 or newer**: Our programming language of choice. Download it from [the official Python website](https://www.python.org/downloads/).
- **Poetry**: This tool helps manage our project's dependencies. Installation instructions can be found on [the Poetry website](https://python-poetry.org/docs/#installation).
- **Protocol Buffers Compiler (`protoc`)**: While optional, it's recommended for generating gRPC code. It's typically named `protobuf` on Linux distributions and can be installed via Homebrew on macOS with `brew install protobuf`.

Additionally, you'll need to download the `bos-public-api` repository and place it in the project root in a folder named `./bos-public-api`. [the bos-public-api official repo](https://github.com/braiins/bos-plus-api)

### Setup

Follow these steps to get your development environment ready:

1. **Clone the repository**: This copies the project files onto your computer.
    ```bash
    git clone --recurse-submodules https://github.com/braiins/bos-api-demo.git
    cd bos-api-demo/python
    ```

2. **Install dependencies with Poetry**: This step fetches all necessary libraries.
    ```bash
    poetry install
    ```

3. **Prepare the `bos-public-api`**: If you haven't already, download the [bos-public-api](https://github.com/braiins/bos-plus-api) and ensure it's placed within the project root as `./bos-public-api`.

4. **Generate gRPC code (optional)**: Needed if the gRPC service definitions are updated or not checked into Version Control System (VCS).
    ```bash
    poetry run python scripts/gen-proto.py
    ```

## Usage

To interact with the gRPC API from the client, you need to specify the miner's IP address and port (default is 50051). Here's how:

```bash
poetry run python src/client.py <MINER-IP>:50051
```

Replace `<MINER-IP>` with the actual IP address of the miner you wish to connect to.

## Development

### Regenerating gRPC Stubs

If you modify the `.proto` files, you must regenerate the gRPC Python code accordingly.

```bash
poetry run python scripts/gen-proto.py
```

This step ensures that the Python code used by the gRPC client and server is up to date with your `.proto` definitions.
