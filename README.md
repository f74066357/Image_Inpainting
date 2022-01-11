# Image_Inpainting

## Objective
Implement gated convolution and do experiments including loss function and hyper parameters on training results. What’s more, we provide an easy-use UI for image inpainting.


## Pretrained model
https://download.openmmlab.com/mmediting/inpainting/deepfillv2/deepfillv2_256x256_8x2_places_20200619-10d15793.pth

## Our training model


## Usage
* train
```
python tools/train.py configs/inpainting/deepfillv2/custom.py
```
* inpainting result
```
python demo/inpainting_demo.py configs/inpainting/deepfillv2/custom.py work_dirs/basic/iter_100000.pth examples/case3_input.png examples/case3_mask.png examples/new300.png
```
## try our UI on Colab
https://colab.research.google.com/drive/1XqXebX-RwvoKko5hW7q22ZBe4DpsYC7e?usp=sharing

## Referemce
https://github.com/open-mmlab/mmediting
https://github.com/styler00dollar/Colab-mmediting/tree/master/mmedit/models
