
package main

import (
   "log"
   "github.com/valyala/fasthttp"
)


func main() {
	
    c := fasthttp.Client{}

    // Create a request
    req := fasthttp.AcquireRequest()
    defer fasthttp.ReleaseRequest(req)
    req.SetRequestURI(`https://eksisozluk.com/giris`)

    // Create a response
    resp := fasthttp.AcquireResponse()
	
    defer fasthttp.ReleaseResponse(resp)
	test := c.Do(req, resp)
    // Execute the request, writing to the response object
		log.Printf(resp)



    //  Loop over all cookies; usefull if you want to just send everything back on consecutive requests
    resp.Header.VisitAllCookie(func(key, value []byte) {
        log.Printf("Cookie %s: %s\n", key, value)
    })

    // Read a specific cookie
}