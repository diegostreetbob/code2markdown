[TOC]
## Fuente: testpython
### main() del programa
#### Creaci�n del socket
Para la creaci�n usamos estas tres l�neas:
```python
serverSocket = socket(AF_INET, SOCK_STREAM)
```
```python
serverSocket.bind((gethostname(), 8801))
```
```python
serverSocket.listen(10)
```
> Posteriormente quedamos a la espera de conexi�n por parte de un cliente.
```python
connectionSocket, addr = serverSocket.accept()
```
Si ocurre un error:
```python
connectionSocket.shutdown(SHUT_RDWR)
```
```python
connectionSocket.close()
```
Al acabar siempre cerramos la conexi�n
```python
serverSocket.close()
```
***
