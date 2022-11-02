# Golang gRPC Python

This is a summary of my notes from learning how to use gRPC to call Python code using Golang and vice versa for the first time.

## Quick starts

First go through both quick starts. Both use separate repos and need to be installed.

https://grpc.io/docs/languages/go/quickstart/

https://grpc.io/docs/languages/python/quickstart/


Then, as of this writing, both will connext as is because they use the same format and port.

## Testing

As a test of calling code back and forth, I created this branch will allows the `name` sent to be optional input from Python -> Go.

https://github.com/aaronlelevier/grpc/tree/add-args-to-python-helloworld

## Notes on building

The `protoc` commands only need to be run when changing `.proto` protobuf files.
