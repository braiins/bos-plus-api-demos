package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"

	pb "go-demo/pb/github.com/braiins/bos-plus-api/braiins/bos/v1"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatalf("Usage: %s <server address>", os.Args[0])
	}
	addr := os.Args[1]

	// Set up a connection to the server.
	conn, err := grpc.Dial(addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	authClient := pb.NewAuthenticationServiceClient(conn)
	configClient := pb.NewConfigurationServiceClient(conn)
	actionsClient := pb.NewActionsServiceClient(conn)

	// Reading username and password
	var username, password string
	fmt.Println("Enter username:")
	fmt.Scanln(&username)
	fmt.Println("Enter password:")
	fmt.Scanln(&password)

	// Login
	fmt.Println("Logging in...")
	headerMD := metadata.MD{}
	ctx := context.Background()
	loginReq := &pb.LoginRequest{
		Username: username,
		Password: password,
	}

	_, err = authClient.Login(ctx, loginReq, grpc.Header(&headerMD))
	if err != nil {
		log.Fatalf("could not login: %v", err)
	} else {
		fmt.Println("Login successful")
	}

	authTokens := headerMD.Get("authorization")
	if len(authTokens) == 0 {
		log.Fatal("authorization token not found in headers")
	}
	authToken := authTokens[0] // Taking the first token

	// Attach auth token to context
	md := metadata.New(map[string]string{"authorization": authToken})
	authCtx := metadata.NewOutgoingContext(ctx, md)

	// Get Miner Configuration
	fmt.Println("Fetching miner configuration")
	_, err = configClient.GetMinerConfiguration(authCtx, &pb.GetMinerConfigurationRequest{})
	if err != nil {
		log.Fatalf("could not get miner configuration: %v", err)
	}

	fmt.Println("Trying to pause mining for 30 seconds...")
	// Pause and Resume Mining
	_, err = actionsClient.PauseMining(authCtx, &pb.PauseMiningRequest{})
	if err != nil {
		log.Fatalf("could not pause mining: %v", err)
	}

	time.Sleep(30 * time.Second)

	fmt.Println("Resuming mining")
	_, err = actionsClient.ResumeMining(authCtx, &pb.ResumeMiningRequest{})
	if err != nil {
		log.Fatalf("could not resume mining: %v", err)
	}

	log.Println("Operation successful")
}