
1 代码简洁 -> 常数项低  (-> means imply)


2 实际工程、应用中，为什么不使用递归函数？

-   递归栈 （overflow，深度不定）
-

3 编码 - 解码 （物理结构 - 逻辑结构）

“一个东西本身，有很多种诠释的角度” （一个物理结构，可以模拟多种逻辑结构。换一个诠释的角度，解释规则）

4 排序的稳定性 及 排序稳定性的意义


5 工程中的综合排序算法

```
if N < 60 etc:
    insert_sort()
else:
    if basic data type:  # (don't need consider sort's stable)
        quicksort()
    else:  # complex type (need sort stable)
        merge_sort()
```


----
