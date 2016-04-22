# MATLAB-Python cheatsheet

## Básico

### Estructuras de control

{width=100%}
![](images/linesep.PNG)

**Sentencia if**

{linenos=off}
```matlab
if a>0
    disp('a es positivo');
end
```

{linenos=off}
```python
if a>0:
    print("a es positivo")
```

{width=100%}
![](images/linesep.PNG)

**Bucle for**

{linenos=off}
```matlab
for x=1:10
    disp(x);
end
```

{linenos=off}
```python
for x in range(1,11):
    print(x)
```

{width=100%}
![](images/linesep.PNG)

**Bucle while**

{linenos=off}
```matlab
k = 0;
while k<10
    disp(k);
    k = k + 1;
end
```

{linenos=off}
```python
k = 0
while k<10:
    print(k)
    k += 1
```


## Matrices

{width=100%}
![](images/linesep.PNG)

**Creando una matriz**

```matlab
A = [1,2,3;4,5,6;7,8,9];
```

```python
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
```

{width=100%}
![](images/linesep.PNG)



{width=100%}
![](images/linesep.PNG)



{width=100%}
![](images/linesep.PNG)
