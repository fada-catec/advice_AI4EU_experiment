# ADVICE AI4EU Solution Experiment

ADVICE: AI-baseD predictiVe road maIntenanCE 

## Local Deployment Cheatsheet

install grpcio-tools

1. Install docker

2. Clone this repository and move to "local" branch

3. Copy images to __shared_folder/img__ (1280x720 size)

4. Copy labels to __shared_folder/orig_labels__ (YOLO format)

5. Move to orchestrator directory

6. Run "./start.sh" or "./start.sh -r" to include semantic segmentation node. Run this command twice if it is the first time you pull the docker images 

7. Install [grpcio-tools](https://pypi.org/project/grpcio-tools/) python module 

8. Run "python orchestrator.py"

9. Go to "http://localhost:8004"

10. Follow the LAT instructions

11. New labels will be placed in __shared_folder/new_labels__

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