source ~/.bashrc
export CUDA_VISIBLE_DEVICES=$1
echo --model_name Animate$2
THEANO_FLAGS='device=gpu0, floatX=float32, nvcc.fastmath=True' nohup python -u train_dcgan.py --model_name Animate$2 --save_freq 10 > DCGANAnimate$2.log &