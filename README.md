# Currency exchange API

### Possibilities:
Api allows to obtain actual currency rate on current date according to official Central Bank rates

### Testing
just run pytest

### Routes
root: '/' - just return some heloo message
http://0.0.0.0/api/rates?from=usd&to=rub&value=1 - route to obtain values
required fields:
from - valute name(e.g., 'usd', 'eur', etc)
to - valute name(e.g., 'usd', 'eur', etc)
value - amount, default to 1

returns json 
{"result":"amount"}

Example:
! [] (https://github.com/SpaceSail/CurrencyExchangeAPI/blob/main/img/Снимок%20экрана%202024-10-09%20в%2011.29.16.png)

### Docs: 
0.0.0.0:80/docs

### Deployment
`gh repo clone SpaceSail/CurrencyExchangeAPI`

`docker build -t myimage . `

`docker run -d --name mycontainer -p 80:80 myimage`
### NB!
Now running in production mode. Change 'CMD ["fastapi", "run", "app/main.py","--host", "0.0.0.0", "--port", "80"]'
to 'CMD ["fastapi", "dev", "app/main.py","--host", "0.0.0.0", "--port", "80"]' 

