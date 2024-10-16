# Currency exchange API

### Possibilities:
Api allows to obtain actual currency rate on current date according to official Central Bank rates

### Testing
just run pytest

### Routes
root: '/' - just return some helo message

`http://0.0.0.0/api/rates?from=usd&to=rub&value=1` - route to obtain values

required fields:

from - valute name(e.g., 'usd', 'eur', etc)

to - valute name(e.g., 'usd', 'eur', etc)

value - amount, default to 1

returns json 
{"result":"amount"}

Example:

![Required and default fields](https://github.com/SpaceSail/CurrencyExchangeAPI/blob/main/img/3.png)

![Screenshot of 'GET' request](https://github.com/SpaceSail/CurrencyExchangeAPI/blob/main/img/1.png)

![Result of 'GET' request](https://github.com/SpaceSail/CurrencyExchangeAPI/blob/main/img/2.png)


### Curl

`curl -X GET "http://127.0.0.1:80/api/rates?from=usd&to=rub&value=100"
`
### Docs: 
0.0.0.0:80/docs

### Deployment
`gh repo clone SpaceSail/CurrencyExchangeAPI`

`docker build -t myimage . `

`docker run -d --name mycontainer -p 80:80 myimage`
### NB!
Now running in production mode. Change 'CMD ["fastapi", "run", "app/main.py","--host", "0.0.0.0", "--port", "80"]'
to 'CMD ["fastapi", "dev", "app/main.py","--host", "0.0.0.0", "--port", "80"]' 

