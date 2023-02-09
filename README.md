# Prediction-of-continuous-polishing-parameters-based-on-Stacked-LSTM
Traditional continuous polishing technology of optical components relies heavily on the pro-cessing experience of the processing personnel. The surface shape of the pitch lap is judged by frequent offline measurement of the surface shape of the processing workpiece, and then the pro-cessing personnel judges how to adjust the next process parameters through their own experience, which will lead to uncertainty of processing time and low processing efficiency. Based on the historical processing data, including the surface parameters of workpieces and pro-cess parameters before and after each processing, a machine learning-based prediction method of process parameters is proposed. A dual stacked LSTM (Long-Short Term Memory) prediction model is proposed to predict process parameters and workpiece surface parameters respectively. The model implicitly obtains the real-time surface shape information of the pitch lap through the workpiece surface parameters, and predicts the real-time optimal process parameters.

click==           8.1.3
colorama==        0.4.5
et-xmlfile==      1.1.0
future==          0.18.2
joblib==          1.1.0
numpy==           1.23.2
openpyxl==        3.0.10
pandas==          1.4.3
pefile==          2022.5.30
Pillow==          9.2.0
PyQt5==           5.15.7
PyQt5-Qt5==       5.15.2
PyQt5-sip==       12.11.0
python-dateutil== 2.8.2
pytz==            2022.2.1
QPT==             1.0b4.dev6
scikit-learn==    1.1.2
scipy==           1.9.0
setuptools==      61.2.0
six==             1.16.0
sklearn==         0.0
threadpoolctl==   3.1.0
toml==          0.10.2
wget==            3.2
wheel==0.37.1
wincertstore==0.2
