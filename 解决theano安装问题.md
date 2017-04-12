解决theano编译问题
1. nvcc 无法识别编译选项
（1） -sm 52无法识别
    使用的nvcc版本过低，可以用nvcc --version 确定。如果cuda装的是新的，那么版本过低的原因可能是用了久的程序。
    可以用which nvcc确定。一般来说显示/usr/local/cuda/bin/nvcc就是正常了。
    解决方法是调整$PATH变量中的目录顺序，将正确的cuda目录放在最前。
（2） --allow_managed无法识别
    未知原因，路径更改正确后消失。
（3） nvcc 无法识别 cpu_arch
    CUDA_ROOT可能又问题，可以在~/.theanorc中设定

2. nvlink fatal
（1）可能也是版本不对。要求与nvcc版本一致。

cuDNN无法识别问题

1. /usr/bin/ld 无法找到-lcudnn
一般来说libcudnn如果装上了，应该是在cuda目录下的lib64目录下。
（1）查看$LD_LIBRARY_PATH，确保包含该路径。
（2）确保其他路径没有重复的库
（3）运行ldconfig

2. gcc: error: /usr/bin/crt/link.stub: No such file or directory
强行将cuda下bin/crt加到$PATH中。

3. 无法找到cudnn.h
将cuda下include加入到$PATH中

如果还有问题，不妨参考atlantix的.bashrc和.theanorc