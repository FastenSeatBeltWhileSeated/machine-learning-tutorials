# Machine Learning Tutorials — Reference Collection

A personal reference fork of [TannerGilbert/Tutorials](https://github.com/TannerGilbert/Tutorials), originally authored by **Gilbert Tanner**.

This repository contains third-party teaching material. The changes in this fork organize the collection and remove generated IDE/build files; the tutorial implementations are preserved.

## Browse the collection

| Topic | Category | Preserved files |
| --- | --- | --- |
| [A guide to Ensemble Learning](tutorials/machine-learning/ensemble-learning) | machine-learning | 9 |
| [Deploying your ML Model](tutorials/deployment/flask) | deployment | 7 |
| [Discord Sentiment Analysis Bot](tutorials/integrations/discord-sentiment) | integrations | 6 |
| [FastAI](tutorials/deep-learning/fastai) | deep-learning | 7 |
| [Google Coral USB Accelerator](tutorials/computer-vision/coral-usb) | computer-vision | 3 |
| [Introduction to Data Visualization in Python](tutorials/data-analysis/visualization) | data-analysis | 4 |
| [Introduction to Deep Learning with Keras](tutorials/deep-learning/keras-introduction) | deep-learning | 1 |
| [Introduction to Machine Learning in C# with ML.NET](tutorials/machine-learning/mlnet-credit-card-fraud) | machine-learning | 7 |
| [Introduction to Web Scraping with BeautifulSoup](tutorials/data-collection/beautifulsoup-introduction) | data-collection | 1 |
| [Keras-Tutorials](tutorials/deep-learning/keras-series) | deep-learning | 26 |
| [Machine-Learning-Explained](tutorials/machine-learning/linear-regression) | machine-learning | 2 |
| [Recommendation System](tutorials/machine-learning/recommendation-system) | machine-learning | 9 |
| [Reddit Webscraping using PRAW](tutorials/data-collection/reddit-praw) | data-collection | 2 |
| [Scikit-Learn-Tutorial](tutorials/machine-learning/scikit-learn) | machine-learning | 15 |
| [Streamlit](tutorials/deployment/streamlit) | deployment | 12 |
| [Tensorflow Object Detection](tutorials/computer-vision/tensorflow-object-detection) | computer-vision | 9 |
| [TensorflowJS-Tutorials](tutorials/deep-learning/tensorflowjs) | deep-learning | 10 |
| [Uber Ludwig Examples](tutorials/deep-learning/ludwig-examples) | deep-learning | 14 |
| [Uber Ludwig Introduction](tutorials/deep-learning/ludwig-introduction) | deep-learning | 4 |
| [VuePress Documentation Website](tutorials/documentation/vuepress) | documentation | 4 |
| [Web Scraping using Selenium and BeautifulSoup](tutorials/data-collection/selenium-beautifulsoup) | data-collection | 10 |

## Structure

- `tutorials/`: 21 topic folders grouped into eight categories.
- `docs/`: source provenance, migration records and known runtime limitations.
- `scripts/check_structure.py`: verifies preserved file hashes and cleanup.
- `UPSTREAM_README.md`: the original author's README.
- `LICENSE`: the original MIT notice, preserved unchanged.

## Using a tutorial

Enter the topic's folder and read its own README or notebook instructions. For examples that use local datasets, start the script or Jupyter session from the directory containing those files.

Each example may require its own environment and dependency versions. There is no single root environment that runs this whole collection. Some examples use historical APIs, external datasets, provider services or machine-specific paths; see [runtime notes](docs/runtime-notes.md).

## Verify the reorganization

```bash
python scripts/check_structure.py
```

This validates paths and original Git blob hashes. It does not execute the tutorials or establish compatibility with current libraries.

## Attribution

All preserved teaching material remains credited to its original author. Structural changes in this fork do not imply authorship of the original models, articles or algorithms.

See [provenance](docs/provenance.md), [the upstream README](UPSTREAM_README.md) and [LICENSE](LICENSE).
