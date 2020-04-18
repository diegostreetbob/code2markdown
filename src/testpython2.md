[TOC]
## Fuente: testpython2.py
### main() del m�dulo 2
#### Creaci�n del socket
Para la creaci�n usamos estas tres l�neas:
`serverSocket = socket(AF_INET, SOCK_STREAM)`

`serverSocket.bind((gethostname(), 8801))`

`serverSocket.listen(10)`

> Posteriormente quedamos a la espera de conexi�n por parte de un cliente.
```python
connectionSocket, addr = serverSocket.accept()
```
`mensaje = connectionSocket.recv(1024)`

Si ocurre un error:
`connectionSocket.shutdown(SHUT_RDWR)`

`connectionSocket.close()`

Al acabar siempre cerramos la conexi�n
`serverSocket.close()`

***
*Sello temporal:18-Apr-2020 (11:32:50.321672)*
*Documentado con code2markdown, https://github.com/diegostreetbob/code2markdown*