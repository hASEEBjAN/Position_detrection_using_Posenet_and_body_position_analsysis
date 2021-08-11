# Installation


```
pip install -r requirements.txt
```

# How to Run?

```
python inference.py --path=input/example_standing.jpg --model=II --framework=tflite --visualize --store
````

- The above command saves coordinates of body parts in a CSV file and overlays detected points over the original image.
- Outputs can be found in same folder as input image. Sample Input/Output can be found in "input folder"

# About the Alogrithm

- The algorithm were created and testing in algorithm.py 
- After successful calculation of angles between hip-knee and ankle-knee. Then it were imported to helper.py the name of the method were display_position
- Then that helper.display_position were called in annotate_image annotate_video methods in inference.py
- The output were shown in the terminal as well as on the image output in the input folder.
# Results
- For the standing the image which I feeded were,
![Feeded Standing](https://github.com/hASEEBjAN/Position_detrection_using_Posenet_and_body_position_analsysis/blob/main/input/example_standing.jpg)
and the output which the model gave were,
![Get Standing](https://github.com/hASEEBjAN/Position_detrection_using_Posenet_and_body_position_analsysis/blob/main/input/example_standing_tracked.png)
- For the sitting the image which were feeded,
![Feed Sitting](https://github.com/hASEEBjAN/Position_detrection_using_Posenet_and_body_position_analsysis/blob/main/input/sitting.jpg)
and the output were,
![getted sitting](https://github.com/hASEEBjAN/Position_detrection_using_Posenet_and_body_position_analsysis/blob/main/input/sitting_tracked.png).
