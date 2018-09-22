## Supervised Leaning (监督学习)
1.  establish notation(机器学习符号) 
>  input variables(输入变量)
$$x^{(i)}$$
> target variable(输出变量)
$$y^{(i)}$$
> training example ()
$$(x^{(i)},y^{(i)}) $$
> training set (训练集)
$$\{((x^{(i)},y^{(i)}); i=1,....m)\}$$
"i" index into the training set;
$$ h(x) = X->Y $$
>function h is called a hypothesis
- Linear Regression(线性回归)
	1. supervised learning(监督学习)
	>decide to approximate y as a linear function of x
	>$$h_\theta(x) = \theta_0 + \theta_1x_1 + \theta_2x_2$$
	>To simplify our notation, we also introduce the convention of letting 
	$$x_0= 1$$  
	>(this is the **intercept term(权重)**), So
	$$h_{(x)} = \sum_{i=0}^n\theta_ix_i=\theta^Tx$$
	2. 
