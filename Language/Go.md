 # Go
 - C style with garbage collector
 - In case of sending in a function
    - If intension to modify then pass by reference - Mutation Function
    - if not pass by value



## Code snippet
 ```go
 // Go code will not run with redundent import
 // Remove imports and sort
goimports -w *.go
 ```


 ```go
type Person struct {
    name string
}

func (p *Person) Info() string {
    if p==nil {
        return ""
    }
}

var test *Person
// Here reciever treated as first parameter
test.Info()
Info(test)
 ```


 # Resources
 - https://word.bitly.com/post/29550171827/go-go-gadget
 - https://www.youtube.com/watch?v=xSq0OdlVLRI&list=PLoiT1Gv2KR1gE-WK7dIQ5bsJ_RAVZnzP8&index=1 