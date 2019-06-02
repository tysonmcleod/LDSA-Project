# LDSA-Project

## Project Report

Our project report can be found on: [Overleaf](https://www.overleaf.com/read/jrqcwqnztjtc)



## Project Presentation

Our project report can be found on: [Google Slides](https://docs.google.com/presentation/d/179DqzOYCw_wOeDz_wg5O66ERLB3PrQHujAAJIpTWGfs/edit?usp=sharing)

## Yelp Dataset

Make sure to download the dataset (from Kaggle - [Download Dataset](https://www.kaggle.com/yelp-dataset/yelp-dataset?fbclid=IwAR0CANuIFCnhG41B_k7IttjUD0YyaabOMAtweiQ2t52do0pvX9rKkEih6Tw) or Yelp directly - [Download Dataset](https://www.yelp.com/dataset), extract the `.tar.gz` or `zip` files and place all `JSON` files inside the `data` folder (e.g., `./data/yelp_academic_dataset_business.json`).

**Note:** Please be aware that these are not actual `JSON` files but text-files containing a valid `JSON` per line.

## Installation

**Requirements**

- `Anaconda` or `Conda` must be installed
- `PySpark` needs to be installed. Google for PySpark Instllation on Mac/Windows/Linux.

**Installation**

- run the script in the `setup` folder: `python setup.py`
- a new conda environment called: `pyspark` will be created and all dependencies installed.
- quickly install `nltk`: pip install nltk 
- afterwards, run `activate pyspark` and `jupyter notebook`.
- now, you should be ready to start with the notebook.

## Execution

Once the Jupyter notebook is up and running:

1. configure the execution mode (local vs. remote), set the boolean in the setup instructions
2. specifiy the resources (e.g., the number of instances, memory, cores, etc.)
3. write everything down in the `experiments.csv`
4. during the experiment, verify on `http://localhost:4040` that the specified resources are actually allocated and the experiment is run as intended.

## Evaluation

The raw resuls of the experiments can be found in `./results/experiments.csv`.

The file is composed of five columns: `Number`, `ExperimentData` (with which data did we perform the experiment - e.g., business, users, reviews), `ExecutionMode` (was the experiment run locally or deployed and with how many resources), `TimeTaken` (the time taken per experiment), `Comments`
