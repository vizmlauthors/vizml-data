# VizML: Training Data and Features

This repository provides access to the **Plotly dataset-visualization pairs**, **feature extraction scripts**, and **features** used in the VizML paper. In the near future, we this repository will include train-test splits, code for training machine learning models, the final serialized models, and the gold standard data subset used in the crowdsourced evaluation.

<img src="assets/flow.png" width="500" />

## Data Description
We provide a **subset** of the Plotly corpus with 10K pairs, the **full corpus** with 1,066,443 pairs (205G), and **features** extracted from an aggressively deduplicated set of 119,815 pairs (19G). More information about the corpus schema, the extracted features, and the design choices are providing in the paper.

## Contents
```
vizml-data
  └───retrieve_data.sh: Shell script to download and unzip dataset-visualization pairs and features
  └───feature_extraction/: Modules for extracting and aggregating features from datasets
      └───extract.py: Entry point for extracting features
  └───preprocessing/: Scripts to preprocess features before ML modeling
  └───assets/: Miscellaneous material for documentation
```
