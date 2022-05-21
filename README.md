<br>

## <div align="center">Audio Emotion Detection</div>

<details open>
<summary>Introduction</summary>
Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) on Kaggle is used. In the dataset, there are totally 8 emotions including calm, happy, sad, angry, fearful, surprise, and disgust expressions. Each expression is produced at two levels of emotional intensity (normal, strong), with an additional neutral expression. There are 12 males and 12 females recording audios.

The task is to visualize audio MP4 file into **Mel-Spectrograms** images and apply CNN + LSTM to estimate sequential images.

</details>

<details open>
<summary>Methodology</summary>

Pipeline of audioemotion detection is as follows:
  
![image](https://user-images.githubusercontent.com/72702872/169657071-3aaa1789-1a39-4fef-8d28-856c25de0895.png)

<details open>
<summary>Data Preprocess</summary>

- Transferring MP4 audio file to Mel-Spectrograms:

  In this task, to achieve prediction of audio motion, we transferred MP4 files to Mel-Spectrograms images with sequence information in it. Pipeline of transferring MP4 audio file to Mel-Spectrograms is as follows:
  
  ![image](https://user-images.githubusercontent.com/72702872/169658800-0fa1230c-e94d-4227-af62-37af97b01e69.png)

  
  Mel-Spectrograms has the following merits when dealing with signals:
  
  (1). Spectrogram is able to split different component within audio signal so that we can find out possible features.
  
  (2). Mel is a algorithms to identify difference between high-frequence sound more clearly. My introducing Mel-Spectrograms, we try to prepare the audio files to well-prepared images containing information of audio emotion.
  
  ![image](https://user-images.githubusercontent.com/72702872/169658825-b1a40927-332d-4073-bbd8-1131d15c211d.png)

</details>  

<details open>
<summary>Model Training</summary>

The detailed structure of the model is as follows:
  
![image](https://user-images.githubusercontent.com/72702872/169658893-177915f4-e939-44fc-b7e2-db89978f3759.png)

</details>

</details>

<details open>
<summary>Result</summary>
  
<details open>
<summary>Model Performance</summary>

![image](https://user-images.githubusercontent.com/72702872/169658939-81d88433-aa89-4f00-9853-6448d5a525e8.png)

</details>

</details>

<details open>
<summary>Reference</summary>

[1] World Meteorological Organization (WMO). 2009. Weather and Climate Change 
Implications for Surface Transportation in the USA. Available at https://public.wmo.int/ 
as of 2009.

[2] United States Department of Transportation. 2020. Transportation Statistics Annual 
Report 2020 Available at https://fdd.bts.gov/freight-data-dictionary/ as of 2020

[3] U.S. Energy information Administration. 2020. Available at https://www.eia.gov/ as of 
2020

[4] Quora Answer Board. 2020 Available at https://www.quora.com/How-many-milescan-the-average-semi-truck-pull-a-full-load-without-refueling as of 201

</details>

</details>

## <div align="center">Contact</div>

email: likehao1006@gmail.com

LinkedIn: https://www.linkedin.com/in/kehao-li-06a9a2235/

ResearchGate: https://www.researchgate.net/profile/Gorden-Li

<br>

