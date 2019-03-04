# PySpark-Transformations

Doing some of the Katas of Chandni Patel in her repo:
https://github.com/chandnipatelTW/transformations 

## Pre-requisites
Please make sure you have the following installed
* Conda with Python 3.X installed (maybe pip works as well!)  
* Apache Spark 2.4 with ability to run spark-submit

## Setup Process
* Clone the repo
* `cd [the-repo]`
* Create the conda env:
```
conda create -n [yourenvname]
conda activate [yourenvname]
conda install pip
```
* Run `make all` to run the tests and create build the project

## Running the tests
```
make test 
```
## Running Data Apps
* Package the project with
``` 
make build
``` 
* Sample data is available in the dist directory

### Wordcount
This applications will count the occurrences of a word within a text file. By default this app will read from the words.txt file and write to the target folder.  Pass in the input source path and output path directory to the spark-submit command below if you wish to use different files. 

```
cd dist 
spark-submit --py-files jobs.zip,libs.zip main.py --job wordcount
```

now in `dist/resources/` you are going to see your wordcount folder, yes it is a folder (and a feature :)): https://stackoverflow.com/questions/24371259/how-to-make-saveastextfile-not-split-output-into-multiple-file 

### Note

Inspiration to how to run spark jobs was taken from:
https://developerzen.com/best-practices-writing-production-grade-pyspark-jobs-cb688ac4d20f
and 
https://github.com/ekampf/PySpark-Boilerplate

 
