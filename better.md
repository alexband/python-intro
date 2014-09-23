```
➜  ~  python -m timeit "s=0" "for i in range(101): s+=i"
100000 loops, best of 3: 7.3 usec per loop
➜  ~  python -m timeit "s=0" "s=sum(range(101))"
100000 loops, best of 3: 2.19 usec per loop
➜  ~  python -m timeit "s=0" "s=sum(xrange(101))"
1000000 loops, best of 3: 1.47 usec per loop
➜  ~  python -m timeit "s=0" "s=(1+100)*100/2"
10000000 loops, best of 3: 0.138 usec per loop
```

