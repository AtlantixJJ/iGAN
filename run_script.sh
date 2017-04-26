export CUDA_VISIBLE_DEVICES=$1
echo --model_name Animate$2
THEANO_FLAGS='device=gpu0, floatX=float32, nvcc.fastmath=True' python iGAN_script.py --model_name Animate$2 --datalist tdlist.txt