
import grpc
import sys
import os

# Import the generated classes
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_dir, 'proto'))
from bos.v1 import authentication_pb2, authentication_pb2_grpc

def run_login(endpoint, username, password):
    # Create a channel and a stub
    channel = grpc.insecure_channel(endpoint)
    stub = authentication_pb2_grpc.AuthenticationServiceStub(channel)

    # Create a login request
    login_request = authentication_pb2.LoginRequest(username=username, password=password)

    # Call the login RPC
    try:
        login_response = stub.Login(login_request)
        print("Login successful.")
        return True
    except grpc.RpcError as e:
        print(f"Login failed: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: client.py <server_endpoint>")
        sys.exit(1)

    endpoint = sys.argv[1]
    username = input("Enter username: ")
    password = input("Enter password: ")

    info = run_login(endpoint, username, password)

    if run_login:
        print("Logged in successfully.");
