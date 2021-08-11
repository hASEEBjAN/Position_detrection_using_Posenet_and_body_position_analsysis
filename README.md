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
