# img2text
A command line script to convert images to text 

## Usage:
Different ways to use https :
*Hello World:

 $ https httpie.io/hello
*Synopsis:

 $ http [flags] [METHOD] URL [ITEM [ITEM]]
*See also http --help.

## Options:
*Options and descriptions : 
 *having a custom HTTP method, headers, and JSON data 
  $ http PUT pie.dev/put X-API-Token:123 name=John
  
 *submitting forms :
  $ http -f POST pie.dev/post hello=World
  
 *Seeing a request that was sent by using an output option :
  $ http -v pie.dev/get
  
 *Building print of a request without having to send it while offline :
  $ http --offline pie.dev/post hello=offline
  
 *Using gitHub API to post a comment on a issue with permission :
  $ http -a USERNAME POST https://api.github.com/repos/httpie/httpie/issues/83/comments body='HTTPie is awesome! :heart:'
  
 *Uploading a file with a redirected input :
  $ http pie.dev/post < files/data.json
  
 *Downlading a file by using a redirected input :
  $ http pie.dev/image/png > image.png
  
 *Downlading a file and saving it with a redirected output
  $ http --download pie.dev/image/png
  
 *Downloading a file wget style :
  $ http --download pie.dev/image/png
  
 *Using named sessions to create certian aspects of communication presistent between requests to the same person or host :
  $ http --session=logged-in -a username:password pie.dev/get API-Key:123

  $ http --session=logged-in pie.dev/headers
  
 *Setting a custom host leader to work on missing DNS records :
  $ http localhost:8000 Host:example.com
