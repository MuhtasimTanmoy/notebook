 # Go
 - C style with garbage collector
 - In case of sending in a function
    - If intention to modify then pass by reference - Mutation Function
    - if not pass by value

```bash
# install go
mkdir ~/go
export GOPATH = "$HOME/go"
echo $GOPATH

mkdir -p $GOPATH/src/github.com/repo_name
cd GOPATH/src/github.com/repo_name
git clone repo_name

go test folder_name/*.go

```

### Code snippet
 ```go
 // Go code will not run with redundant import
 // Remove imports and sort
goimports -w *.go

type Person struct {
 name string
}

func (p *Person) Info() string {
    if p==nil { return "" }
}

var test *Person
// Here receiver treated as the first parameter
test.Info()
Info(test)

go test foo_test.go foo.go
go test server *.go
go run --race test.go 
go vet
```

### References
 - [Go Go Gadget](https://word.bitly.com/post/29550171827/go-go-gadget)
 - [Intro to Git & GO](https://www.youtube.com/watch?v=xSq0OdlVLRI&list=PLoiT1Gv2KR1gE-WK7dIQ5bsJ_RAVZnzP8&index=1)
 - [How to use interfaces in Go](https://jordanorelli.com/post/32665860244/how-to-use-interfaces-in-go)