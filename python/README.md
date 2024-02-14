
# bos-api-demo

## Installation

### Prerequisites

- Python 3.8 or newer
- Poetry for dependency management
- It may be a good idea to have `protoc` installed natively in your system. Typically
  this package will be called `protobuf` on most Linux distributions and in Homebrew.

### Setup

1. Clone the repository:
    ```bash
    git clone --recurse-submodules https://github.com/braiins/bos-api-demo.git
    cd bos-api-demo/python
    ```

2. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

3. Generate gRPC code (optional, if not checked into VCS):
    ```bash
    poetry run python scripts/gen-proto.py
    ```

## Usage

To call the gRPC API from the client:

```bash
poetry run python src/client.py
```

## Development

### Regenerating gRPC Stubs

If you modify the `.proto` files, regenerate the gRPC Python code:

```bash
poetry run python scripts/gen-proto.py
```

