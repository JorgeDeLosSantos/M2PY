# MATLAB-Python cheatsheet

## Básico

### Estructuras de control

{width=100%}
![](images/linesep.PNG)

**Sentencia if**

```matlab
if a>0
	disp('a es positivo');
end
```

```python
if a>0:
	print("a es positivo")
```

{width=100%}
![](images/linesep.PNG)

**Bucle for**

```matlab
for x=1:10
	disp(x);
end
```

```python
for x in range(1,11):
	print(x)
```

{width=100%}
![](images/linesep.PNG)


### Bucle while

```matlab
k = 0;
while k<10
	disp(k);
	k = k + 1;
end
```

```python
k = 0
while k<10:
	print(k)
	k += 1
```

