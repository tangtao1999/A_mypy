import numpy as np
class Perceptron(object):
    """
    这是一个分类器
    """
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        pass
    def fit(self, X, y):
        """

        :param X: 训练样本集
        :param y: 训练样本所对应的分类
        例如X=[[1,2,3],[4,5,6],[7,8,9],[11,12,13]],代表这个样本集中有四个样本，
        每个样本有三个特征值，这三个特征值就是要输入到神经网络中的输入值
        y=[1,1,-1,-1]，代表这四个样本的所属分类
        """
        self.w_ = np.zeros(1 + X.shape[1])
        """
        将权值向量初始化为0向量，因为认为的增加了一个w0，所以要加1
        
        shape函数的解释，依然以上面的例子为例：
        shape是有两个参数的
        shape(nsamples,nfeatures)
        X.Shape[0]就是4
        X.shape[1]就是3
        进一步解释，如果X'=[[[1],[2]][[3],[4]][[5],[6]][[7],[8]]]
        X'.shape[0]=4
        X'.shape[1]=2
        X'.shape[2]=1
        """
        self.errors_ = []
        """
        这个只是一个简单的用来保存错误个数的数组
        """
        """
        下面的循环在我们指定的n_iter次循环下对权值进行更新
        """
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):#zip函数的作用，还以上述为例，zip函数作用后会得到[[1,2,3,1][14,5,6,1][7,8,9,-1][11,12,13,-1]]
                update = self.eta*(target-self.predict(xi))
                #target是样本本该属于的分类，preddict函数时我们预测的分类，在下面会实现

                #下面是对权值的更新
                self.w_[1:] += update*xi
                self.w_[0] += update

                #上式中，如果target与我们自己预测的值相等，会有update值为0，此时errors不会增加，否则按下式中errors值加1
                errors += int(update != 0)

                #将每次循环得到的errors的值放到errors_数组中
                self.errors_.append(errors)
                pass
            pass


        """
        下面的函数就是求权值和的函数
        """
        def net_input(self, X):
            return np.dot(X, self.w_[1:])+self.w_[0]
            pass

        """
        将权值和函数得到的函数值作为下面函数（即为激活函数）的自变量，得到预测的分类
        """
        def predict(self, X):
            return np.where(net_input(self, X) >= 0.0,1 ,-1)
            pass
        pass