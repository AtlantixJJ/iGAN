Theano: 符号化计算图
theano.tensor : 变量 | 只在运行时有值和形状，声明时只有维度和类型
theano.shared : 参数（变量） | 具有初值和形状
表达式与计算图：变量与参数调用已有的运算符号形成的
theano.function(inputs=[],outputs=[],updates=[(old,new)])
将表达式的输入与输出变成函数，并可以改变参数的值
其中有优化、转化成GPU等部分，转化过程为‘编译’
