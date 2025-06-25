package main

import (
	"context"
	"log"
	"net"

	"github.com/sereschen/grpc-test/go/greeter"
	"google.golang.org/grpc"
)

// server is used to implement greeter.GreeterServer.
type server struct {
	greeter.UnimplementedGreeterServer
}

// SayHello implements greeter.GreeterServer
func (s *server) SayHello(ctx context.Context, in *greeter.HelloRequest) (*greeter.HelloReply, error) {
	log.Printf("Received: %v", in.GetName())
	return &greeter.HelloReply{Message: "Hello " + in.GetName()}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	greeter.RegisterGreeterServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
