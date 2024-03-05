# Go

Welcome to the Go version of the `bos-api-demo` project! This guide is designed to assist you in setting up and utilizing this project efficiently, catering to both newcomers and seasoned users of Go, gRPC, Protocol Buffers, and related technologies.

## Installation

Before we begin, let's ensure you have all the necessary tools installed.

### Prerequisites

You'll need the following tools and libraries for this project:

- **Go 1.22 or newer**: The primary programming language used here. Download it from [the official Go website](https://golang.org/dl/).
  - Note that older versions of Go might work just as well
- **Protocol Buffers Compiler (`protoc`)**: Necessary for generating gRPC code from `.proto` files. On Linux, it's typically available through the package manager (often the package is called `protoc` or `protobuf`), while on macOS, you can install it using Homebrew with `brew install protobuf`.
- **Go plugins for the Protocol Buffers Compiler**: These can be installed by running:
    ```bash
    go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
    go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
    ```

### Setup

1. **Clone this repository** and fetch its submodules:
    ```bash
    git clone --recurse-submodules https://github.com/braiins/bos-api-demo.git
    cd bos-api-demo/go
    ```

    If the repository was cloned without submodules, initialize and update them with:
    ```bash
    git submodule update --init --recursive
    ```

2. **Initialize the Go module** (if not done previously):
    ```bash
    go mod init go-demo
    ```

    This command sets up a new Go module, effectively managing your project's dependencies.

3. **Install Go dependencies**:
    Go will automatically manage dependencies when you build or run the program.

4. **Generate gRPC code**:
    Generate the necessary Go code for gRPC from the `.proto` definitions located in the submodule:
    ```bash
    protoc -I ../bos-plus-api/proto ../bos-plus-api/proto/bos/v1/*.proto --go_out=pb --go-grpc_out=pb
    ```
    Run this command from the `go` directory within your project. It's essential whenever the gRPC service definitions are updated.

## Usage

To interact with the gRPC API, specify the miner's IP address and port (defaulting to 50051):

```bash
go run client/main.go <MINER-IP>:50051
```

Replace `<MINER-IP>` with the actual IP address of the target miner.

## Development

### Regenerating gRPC Stubs

Should the `.proto` files within the `bos-public-api` submodule change, regenerate the gRPC Go code to ensure the client and server codes remain synchronized with the `.proto` definitions:

```bash
protoc -I ../bos-plus-api/proto ../bos-plus-api/proto/bos/v1/*.proto --go_out=pb --go-grpc_out=pb
```

Execute this command from within the `go` directory of this project.