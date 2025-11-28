This project implements a real-time Driver Behaviour Monitoring System using Deep Learning, CNN, and OpenCV. The system detects whether a driver’s eyes are open or closed and triggers an alarm when drowsiness is detected continuously. It uses InceptionV3 (pre-trained on ImageNet) as the feature extractor, combined with custom CNN layers for classification.
Real-time drowsiness detection using webcam

CNN model built on top of InceptionV3.

Eye-state classification: Open / Closed.

Automatic alarm when drowsiness score crosses threshold.

Image preprocessing & augmentation.

Trained on custom dataset of eye images.

How It Works:

The webcam captures the driver’s face.

Haar cascades detect the face and eyes.

Each eye image is preprocessed (resize → normalize).

The CNN model classifies the eye state.

A score is maintained—if "closed" is detected repeatedly, an alarm is played.
Technologies Used:

Python, OpenCV, NumPy.

TensorFlow / Keras.

InceptionV3 CNN architecture.

Pygame (for alarm sound)
Model Performance:

Evaluated on train, validation, and test datasets.

Achieves reliable classification for open vs closed eyes.

Optimized using callbacks for better accuracy and reduced overfitting.
PURPOSE:
This project aims to reduce road accidents caused by driver fatigue by providing a real-time automated alerting system.
