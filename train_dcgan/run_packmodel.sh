source ~/.bashrc
export CUDA_VISIBLE_DEVICES=$1
echo --model_name Animate$2
THEANO_FLAGS='device=gpu0, floatX=float32, nvcc.fastmath=True' python -u pack_model.py --model_name Animate$2