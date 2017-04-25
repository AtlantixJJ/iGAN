export CUDA_VISIBLE_DEVICES=$1
echo --model_name Animate$2
THEANO_FLAGS='device=gpu0, floatX=float32, nvcc.fastmath=True' nohup python -u batchnorm_dcgan.py --model_name Animate$2 > ESBNAnimate$2.log &3