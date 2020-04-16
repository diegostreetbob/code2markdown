[TOC]
## Fuente: testpython
### main() del programa
#### Creación del socket
Para la creación usamos estas tres líneas:
```python
serverSocket = socket(AF_INET, SOCK_STREAM)
```
```python
serverSocket.bind((gethostname(), 8801))
```
```python
serverSocket.listen(10)
```
> Posteriormente quedamos a la espera de conexión por parte de un cliente.
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
Al acabar siempre cerramos la conexión
```python
serverSocket.close()
```
***
