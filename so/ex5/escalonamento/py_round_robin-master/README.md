# py_round_robin

你可以直接pip安装
pip install py_round_robin


```
from py_round_robin import Round_Robin
rr_obj = Round_Robin(['a','b','c'])
for i in range(50):
    print rr_obj.get_next()
```


测试的结果:
```
[ruifengyun@spiderman rr (master ✗)]$ python Round_Robin.py
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'a')
(5, 'b')
(6, 'c')
(7, 'a')
(8, 'b')
(9, 'c')
(10, 'a')
(11, 'b')
(12, 'c')
(13, 'a')
(14, 'b')
(15, 'c')
(16, 'a')
(17, 'b')
(18, 'c')
(19, 'a')
(20, 'b')
(21, 'c')
(22, 'a')
(23, 'b')
(24, 'c')
(25, 'a')
(26, 'b')
(27, 'c')
(28, 'a')
```

##TODO

1. Add future ,support weight
