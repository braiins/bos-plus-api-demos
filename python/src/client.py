import grpc
import time
import sys
import os

# Import the generated classes
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_dir, 'proto'))

from bos.v1 import authentication_pb2, authentication_pb2_grpc
from bos.v1 import configuration_pb2, configuration_pb2_grpc
from bos.v1 import actions_pb2, actions_pb2_grpc

def run_login(channel, username, password):
    # Create a stub
    stub = authentication_pb2_grpc.AuthenticationServiceStub(channel)

    # Create a login request
    login_request = authentication_pb2.LoginRequest(username=username, password=password)

    # Call the login RPC
    try:
        response_future = stub.Login.future(login_request)
        response = response_future.result()
        headers = response_future.initial_metadata()
        print("Login successful. Headers:", headers)
        return headers[0].value # auth token

    except grpc.RpcError as e:
        print(f"Login failed: {e}")
        return False

def get_miner_config(channel, auth_token):
    stub = configuration_pb2_grpc.ConfigurationServiceStub(channel)
    cfg_request = configuration_pb2.GetMinerConfigurationRequest()

    try:
        # We need to include the auth token in the metadata
        cfg_response = stub.GetMinerConfiguration(cfg_request, metadata=[("authorization", auth_token)])
        print("Configuration read:")
        print(cfg_response)
        return True
    except grpc.RpcError as e:
        print(f"Reading config failed: {e}")
        return False

def pause_unpause_test(channel, auth_token):
    print("Trying to pause and unpause mining after 30 seconds")
    stub = actions_pb2_grpc.ActionsServiceStub(channel)

    try:
        print("Trying to pause mining")
        pause_request = actions_pb2.PauseMiningRequest()
        pause_response = stub.PauseMining(pause_request, metadata=[("authorization", auth_token)])

        print("Miner response:")
        print(pause_response)

        time.sleep(30)

        print("Trying to resume mining")
        resume_request = actions_pb2.ResumeMiningRequest()
        resume_request = stub.ResumeMining(resume_request, metadata=[("authorization", auth_token)])

        print("Resume response:")
        print(resume_request)
        return True
    except grpc.RpcError as e:
        print(f"Reading config failed: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: client.py <server_endpoint>")
        sys.exit(1)

    endpoint = sys.argv[1]
    username = input("Enter username: ")
    password = input("Enter password: ")

    channel = grpc.insecure_channel(endpoint)

    auth_token = run_login(channel, username, password)

    if auth_token:
        get_miner_config(channel, auth_token)
        pause_unpause_test(channel, auth_token)
