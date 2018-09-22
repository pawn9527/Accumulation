1. 描述梯度下降，随机梯度下降和批量梯度下降的联系与区别?

> - batch gradient descent (批量梯度下降)
	1. algorithm(算法)
	> 
Repeat {
$${\theta{0}}:={\theta{0}}-a\frac{1}{m}\sum\limits{i=1}^{m}{ \left({{h}{\theta }}({{x}^{(i)}})-{{y}^{(i)}} \right)}$$
$${\theta{1}}:={\theta{1}}-a\frac{1} {m}\sum\limits{i=1}^{m}{\left( \left({{h}{\theta }}({{x}^{(i)}})-{{y}^{(i)}}
\right)\cdot {{x}^{(i)}} \right)}$$

> }
	2. 

> -  stochastic gradient descent (随机梯度下降)