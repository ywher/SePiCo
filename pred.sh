TEST_ROOT=$1
CONFIG_FILE="${TEST_ROOT}/*${TEST_ROOT: -1}.json" #143, 
CHECKPOINT_FILE="${TEST_ROOT}/latest.pth" #latest.pth
SHOW_DIR="${TEST_ROOT}/pred_train"
echo 'Config File:' $CONFIG_FILE
echo 'Checkpoint File:' $CHECKPOINT_FILE
echo 'Predictions Output Directory:' $SHOW_DIR
CUDA_VISIBLE_DEVICES=1 python -m tools.test ${CONFIG_FILE} ${CHECKPOINT_FILE} --show-dir ${SHOW_DIR} \
--opacity 0.5 --save_logits --test-set --format-only --eval-option imgfile_prefix=labelTrainIds to_label_id=False  #--aug-test #--eval mIoU
