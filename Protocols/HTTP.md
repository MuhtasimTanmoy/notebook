# HTTP

- In case of Ajax request 'X-Requested-With' headers added. This type of request not something from browser typed.
- Response is ok if `HTTP status code` between 200-299 and if cached status code 304.
- The Host is the domain the request is being sent to. This header was introduced so hosting sites could include multiple domains on a single IP.
- The Origin header is the domain the request originates from.
- The Host header is always included. The Origin header is included sometimes: It is always included on cross-origin requests (across all browsers), and in Chrome/Safari, it is also included on same-origin PUT/POST/DELETE requests. Same-origin GET requests do not include an Origin header.
- CORS (Cross-Origin Resource Sharing) is a system, consisting of transmitting HTTP headers, that determines whether browsers block frontend JavaScript code from accessing responses for cross-origin requests. CORS is a part of HTTP that lets servers specify what hosts are permitted to load content from that server.
- `Access-Control-Allow-Origin: origin-site` CORS response header. The resource determines in response if it can be viewed. Response.set_header("Access-Control-Allow-Origin", "https://yorsite.com")
- The default behavior of cross-origin resource requests is for requests to be passed without credentials like cookies and the Authorization header.
- The cross-domain server can permit reading of the response when credentials are passed to it by setting the CORS Access-Control-Allow-Credentials header to true.
- Some web servers dynamically create Access-Control-Allow-Origin headers based upon the client-specified origin. This is a workaround for CORS constraints that is not secure.
- Testing CORS. Run a server. Access from the devtool console while on different server.
- Preflight options request. 
- Use a proxy to set appropiate headers to access content. https://cors-anywhere.herokuapp.com
- Use of JSONP. Which loads by passing callback. 



# Resources
- https://portswigger.net/web-security/cors/access-control-allow-origin
- https://cors-anywhere.herokuapp.com