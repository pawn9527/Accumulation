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
    > **cost function**
    > $$J(\theta) = \cfrac{1}{2}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2$$
    > **ordinary least squares(最小二乘法)** regression model 
	2. LMS algorithm
	> we want to choose ɵ so as to to minimize J(ɵ)
	>$$ \theta_j := \theta_j - \alpha\cfrac{\partial}{\partial\theta_j}J(\theta) $$
	> **gradient descent algorithm(梯度下降算法)**
	> 阿尔法 is called the learning rate
	3. 
批量梯度下降:
> 指的是在梯度下降的每⼀一步中，我们都⽤用到了了所有的训练样本，在梯度下降中，在      计算微分求导项时，我们需要进⾏行行求和运算，所以，在每⼀一个单独的梯度下降中，我们最终都要计算这样⼀一        个东⻄西，这个项需要对所有 $m$ 个训练样本求和。因此，批量量梯度下降法这个名字说明了了我们需要考虑所有这⼀一"批"训练样本，⽽而事实上，有时也有其他类型的梯度下降法，不不是这种"批量量"型的，不不考虑整个的训练    集，⽽而是每次只关注训练集中的⼀一些⼩小的⼦子集