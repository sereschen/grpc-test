.PHONY: all clean python go

all: python go

python: python/proto/greeter_pb2.py python/proto/greeter_pb2_grpc.py

python/proto/greeter_pb2.py python/proto/greeter_pb2_grpc.py: greeter.proto python/requirements.txt
	python3 -m venv python/.venv
	./python/.venv/bin/pip install -r python/requirements.txt
	mkdir -p python/proto
	./python/.venv/bin/python -m grpc_tools.protoc -I. --python_out=python/proto --grpc_python_out=python/proto greeter.proto

go: go/greeter/greeter.pb.go go/greeter/greeter_grpc.pb.go

go/greeter/greeter.pb.go go/greeter/greeter_grpc.pb.go: greeter.proto
	mkdir -p go/greeter
	protoc --go_out=go/greeter --go_opt=paths=source_relative \
    --go-grpc_out=go/greeter --go-grpc_opt=paths=source_relative \
    greeter.proto

clean:
	rm -rf python/.venv python/proto go/greeter
