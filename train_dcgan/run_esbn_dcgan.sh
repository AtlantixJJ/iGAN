source ~/.bashrc
export CUDA_VISIBLE_DEVICES=$1
echo --model_name AnimateEMDframes$2
THEANO_FLAGS='device=gpu0, floatX=float32, nvcc.fastmath=True' nohup python -u batchnorm_dcgan.py --model_name AnimateEMDframes$2 > BMAnirun$2.log &