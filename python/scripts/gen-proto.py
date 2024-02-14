import subprocess
import sys

def generate_grpc_code():
    proto_path = "./src/api/proto"
    python_out = "./src/proto"
    grpc_python_out = "./src/proto"
    protos = f"{proto_path}/bos/v1/*.proto"
    command = [
        "python3", "-m", "grpc_tools.protoc",
        "-I" + proto_path,
        "--python_out=" + python_out,
        "--grpc_python_out=" + grpc_python_out,
        protos
    ]
    subprocess.run(" ".join(command), shell=True, check=True)

def run_command(command):
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    generate_grpc_code()
    run_command(" ".join(sys.argv[1:]))
