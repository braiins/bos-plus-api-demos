
# bos-api-demo Rust Version

Welcome to the Rust version of the `bos-api-demo` project! This guide aims to streamline the setup and usage of the project, making it accessible for those new to Rust, gRPC, or any other technologies we leverage here.

## Installation

Let's ensure your system is prepared with all necessary tools before starting.

### Prerequisites

To work on this project, you will need:

- **Rust**: The project's programming language. Install Rust by following the instructions on [the official Rust website](https://www.rust-lang.org/tools/install).
- **Cargo**: Rust's package manager and build system, which comes bundled with Rust installations.
- **Protocol Buffers Compiler (`protoc`)**: Necessary for generating gRPC code from `.proto` files. On Linux, it's typically available through the package manager (often the package is called `protoc` or `protobuf`), while on macOS, you can install it using Homebrew with `brew install protobuf`.

### Setup

1. **Clone this repository** to obtain the project files:
    ```bash
    git clone --recurse-submodules https://github.com/braiins/bos-api-demo.git
    cd bos-api-demo/rust
    ```

    Since `bos-public-api` is included as a submodule, ensure it's properly initialized and updated:
    ```bash
    git submodule update --init --recursive
    ```

2. **Build the Project**:
    Rust's build system, Cargo, takes care of fetching dependencies, compiling protocol buffers, and building your project:
    ```bash
    cargo build
    ```

3. **Run the Project**:
    After building, you can run your Rust application directly through Cargo:
    ```bash
    cargo run -- <MINER-IP>:50051
    ```

    Replace `<MINER-IP>` with the actual IP address of the miner you wish to connect to

## Usage

This application interacts with the Braiins OS+ Public API to demonstrate functionalities such as logging in to obtain an authentication token, fetching miner configuration, and controlling mining operations.

To run the application with the required miner IP and port:

```bash
cargo run -- <MINER-IP>:50051
```

Ensure to replace `<MINER-IP>` with the actual IP address of your target miner.

## Development

### Updating Protocol Buffers

While the Rust build process automatically handles the compilation of Protocol Buffers through a `build.rs` script leveraging `tonic-build`, it's crucial to keep the `.proto` files up to date:

- If the `.proto` files in the `bos-public-api` submodule are updated, simply rebuild the project with `cargo build`, and the Rust code will be regenerated to reflect the changes.

### Additional Notes

- Ensure all dependencies are kept up to date by occasionally running `cargo update`.
- For more intricate build configurations or additional proto file adjustments, modifications to the `build.rs` script may be required.

We hope this guide helps you to effectively work with the Braiins OS+ Public API in Rust. Happy coding!
