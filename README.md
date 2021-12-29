# ADVICE AI4EU Solution Experiment

ADVICE: AI-baseD predictiVe road maIntenanCE 

## Local Deployment Cheatsheet

1. Install docker

2. Clone this repository

3. Copy images to __shared_folder/img__ (1280x720 size)

4. Copy labels to __shared_folder/orig_labels__ (YOLO format)

5. Move to orchestrator directory

6. Run "./start.sh" or "./start.sh -r" to include semantic segmentation node

7. Run "python orchestrator.py"

8. Go to "https://0.0.0.0:8004"

9. Follow the LAT instructions

10. New labels will be placed in __shared_folder/new_labels__

## Acknowledgement

***
<img src="./imgs/logo_ai4eu.png" 
     alt="AI4EU" height="45">

Supported by AI4EU - A European AI On Demand Platform and Ecosystem.  
More information: <a href="https://www.ai4europe.eu/">ai4europe.eu</a>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/200px-Flag_of_Europe.svg.png" 
     alt="eu_flag" height="45" align="left" >  

This project has received funding from the European Union's Horizon 2020  
research and innovation programme under grant agreement 825619.


## Help

* Rafael Luque - rluque@catec.aero
* Other community or team contact