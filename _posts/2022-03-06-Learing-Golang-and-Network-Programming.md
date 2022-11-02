# Learning Golang and Network Programming

This blog contains notes on mostly [NTP](http://www.ntp.org/) Learning in conjunction with reading the `ntpc.go` module in this Github repo [vladimirvivien/go-networking](https://github.com/vladimirvivien/go-networking).

## Intro

I have been starting to learn Golang and wanted to start learning why Golang is good for Network Programming. After searching, I found this repo [vladimirvivien/go-networking](https://github.com/vladimirvivien/go-networking). Here are my notes from reading the `ntpc.go` and `ntps.go` modules, mostly the former, in this repo.

## ntpc.go

First, the Packt book is no longer available, so I thought to read [ntpc.go](https://github.com/vladimirvivien/go-networking/blob/master/udp/ntpc/ntpc.go).

Learning about Go, this module starts with:

```go
var host string
flag.StringVar(&host, "e", "us.pool.ntp.org:123", "NTP host")
flag.Parse()
```

Here [flag.StringVar](https://pkg.go.dev/flag#StringVar) is intialized to the address of a pointer, with the default `value` of the 3rd arg, `func StringVar(p *string, name string, value string, usage string)`


Usage:

```bash
// uses default
go run ntpc.go

// uses ntp server from ntps.go
go run ntps.go
go run ntpc.go -e localhost:1123
```

## Golang net pkg

The [net](https://pkg.go.dev/net) pkg is used to create a UDP object, establish a connect then send a request and response. I looked up the us.pool.ntp.org IP information to compare to the Golang objects:


```bash
$ nslookup us.pool.ntp.org
Server:		192.168.1.1
Address:	192.168.1.1#53

Non-authoritative answer:
Name:	us.pool.ntp.org
Address: 70.35.196.28
Name:	us.pool.ntp.org
Address: 168.61.215.74
Name:	us.pool.ntp.org
Address: 216.229.4.69
Name:	us.pool.ntp.org

Address: 66.151.147.38
```

The first Server address is our private network DNS address with th


192.168.0.0/16
Address for private networks (intranets). Such addresses never appear on the public Internet.

## References

https://timetoolsltd.com/ntp/ntp-client/

