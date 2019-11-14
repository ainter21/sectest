# Homework 7
## Giust Alberto Mat. 211460

To resolve this exercise you can't send JSON data because it is blocked by the CORS policy. If you try to send a fetch request from another origin, the website will return a 302 OPTIONS response, and the console will give you an error about CORS policy.

``` html
<html>
<body>
    <script>
        fetch("http://localhost:8081/WebGoat/csrf/feedback/message", {
            method: "POST",
            headers: {
                "Content-Type": "appication/json"
            },
            body: {
                
                "name"    : "WebGoat",
                "email"   : "webgoat@webgoat.org",
                "content" : "WebGoat is the best!!"

            }
        });
    </script>
</body>
</html>

```

![options](/homework-7/options.png)

One of the ways to resolve the exercise is to follow the suggestion given by the article linked at the page. You can create a form with an hidden parameter name that contains the json data and set the encryption as `text/plain`. The website won't block the request because it has normal text, but this text will be interpreted as json, and you can use it to complete teh exercise.

