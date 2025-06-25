import grpc
from proto import greeter_pb2
from proto import greeter_pb2_grpc


def run():
    # 1.  Create a gRPC channel (connection to the server).
    channel = grpc.insecure_channel(
        "localhost:50051"
    )  # Replace with your server address

    # 2.  Create a stub (client) for the service.
    stub = greeter_pb2_grpc.GreeterStub(channel)

    # 3.  Create a request message.
    request = stub.SayHello(greeter_pb2.HelloRequest(name="World"))

    # 4.  Call the gRPC method and get the response.
    try:
        response = stub.GetSomething(request)
        print("Received: " + response.result)
    except grpc.RpcError as e:
        print(f"Error: {e}")
        print(f"Details: {e.details()}")
        print(f"Code: {e.code()}")


if __name__ == "__main__":
    run()
