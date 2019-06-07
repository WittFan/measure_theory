<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=False} -->

<!-- code_chunk_output -->

* [测度论](#测度论)
	* [基本概念](#基本概念)
		* [σ-代数](#σ-代数)
		* [勒贝格σ代数](#勒贝格σ代数)

<!-- /code_chunk_output -->
# 测度论

## 基本概念

### σ-代数
- 定义：
    设$ X $为非空集合，$ {\mathcal {F}} $ 中的元素是 $ X $ 的子集合，满足以下条件的集合系$ {\mathcal {F}} $称为$ X $上的一个σ代数：
    $ X $在$ {\mathcal {F}} $中；
    如果一个集合$ A $在$ {\mathcal {F}} $中，那么它的差集$ A^{c} $也在$ {\mathcal {F}} $中。
    如果有可数个集合$ A_{1},A_{2},\cdots ,A_{n}\cdots $都在$ {\mathcal {F}} $中，那么它们的并集也在$ {\mathcal {F}} $中。<br>  
    用数学语言来表示，就是
    $ X\in {\mathcal {F}}; $
    $ A\in {\mathcal {F}}\Longrightarrow A^{c}\in {\mathcal {F}}; $
    $ (\forall n\in \mathbb {N} ~~~A_{n}\in {\mathcal {F}})\Longrightarrow \bigcup \limits _{n=1}^{\infty }A_{n}\in {\mathcal {F}}. $<br>
    不借助逻辑符号的话，也可以使用如下定义：
    设$ X $为非空集合。则$ X $上的一个σ代数是指其幂集的一个子集合 $ {\mathcal {F}} $， $ {\mathcal {F}} $ 中的元素，在经过<span style="color:#F00">有限个差集、交集或可数个并集这三种运算</span>后依然属于 $ {\mathcal {F}} $，也就是说 $ {\mathcal {F}} $ 对这三运算是<span style="color:#F00">封闭（closed）的 </span>。
<br>
- 概念理解
在测度论里 $ \left(X,{\mathcal {F}}\right) $称为一个可测空间。 集合族 $ {\mathcal {F}} $ 中的元素，也就是 $ X $ 的某子集，称为可测集合。而在概率论中，这些集合被称为随机事件。
是测度论的基础概念之一。
<br>
- 例子：
有两个σ-代数的简单例子，它们分别是：
$ X $上含集合最少的σ代数$ \{\emptyset ,X\} $；和
$ X $上含集合最多的σ代数是$ X $的幂集$ 2^{X}:=\{A:A\subset X\} $。
假设集合$ X=\{a,b,c,d\} $，那么$ {\mathcal {F}}=\{\varnothing ,\{a\},\{b,c,d\},X\} $ 是集合$ X $上的一个σ代数。这也是所有包含$ \{a\} $的σ代数中最“小”的一个。

### 勒贝格σ代数
1901年亨利·勒贝格建立的勒贝格σ代数。而现代的测度理论的公理化体系就建立在勒贝格的相关理论之上。在这个领域中，σ代数不仅仅是用于建立公理体系，也是一个强有力的工具，在定义许多重要的概念如条件期望和鞅的时候，都需要用到。

