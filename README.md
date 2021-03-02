# Ship-block-classification

[ 사용된 CNN 모델 ] 
- DenseNet201
- InceptionV3
- NASNetLarge
- ResNet156V2
- VGG19

[ npy 파일로의 변환 ]
- 대량의 이미지 파일을 CNN 모델이 한번에 학습시킬 수 있도록 npy파일로 변환하여 데이터를 flow합니다.
- 학습이 완료된 CNN 모델의 학습 정확도를 검증하기 위해 구성된 prediction 데이터도 npy 파일로 변환하여 사용 가능합니다.
= npy 폴더에 npy파일로 만들기 위한 이미지를 할당하시오.

[ data augmentation 적용 여부 설정 가능 ]
- exe.py에서 data augmentation 스크립트 활성화 여부 확인

[ Transfer Learning 적용 여부 설정 가능 ]
- exe.py에서 Transfer Learning 정용 여부 설정 가능

------------------------------------------------------------------------------------------------------------------

make_npy_file.py    : npy 폴더 안의 이미지들을 npy파일로 만들어줍니다.
npy_predict.py      : prediction에 사용될 이미지들로 만들어진 npy 파일을 이용해 학습된 모델의 학습 정확도를 검증합니다.
confusion_matrix.py : 모델의 학습정확도를 confusion matrix를 이용해 산출합니다.
plot_history.py     : 모델의 학습 진행 과정을 그래프로 확인할 수 있습니다. (epoch 당 loss, accuracy 확인가능)
image_size_check.py : 학습과 검증에 사용될 image에 사전오류를 확인합니다. (크기 등의 문제)

------------------------------------------------------------------------------------------------------------------

학습 완료된 모델은 Result폴더에 .hdf5 파일로 저장됩니다.
