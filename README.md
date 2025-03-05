<!--
  README.md for LLNewsBias: A Multilingual News Dataset for Lifelong Learning
  This document is intended to provide a comprehensive overview of the project,
  highlight advanced coding practices, and encourage collaboration.
-->

# LLNewsBias: A Multilingual News Dataset for Lifelong Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Build Status](https://img.shields.io/travis/Swati17293/LLNewsBias.svg)](https://travis-ci.org/Swati17293/LLNewsBias)

## Overview

**LLNewsBias** is a multilingual dataset designed to detect and analyze political bias in news headlines. Covering four major global events — Brexit, COVID-19, the 2020 U.S. election, and the Ukraine-Russia war — from 2019 to 2022, the dataset features over **350,000 headlines** in **17 languages**, each annotated with bias labels.  
This resource is structured to support lifelong learning in natural language processing, allowing for event-wise and year-wise analysis.

## Motivation & Objectives

- **Objective:** Improve the detection of political bias in news reporting by leveraging a large-scale, multilingual dataset.
- **Motivation:** With the rapid rise of digital media, ensuring the impartiality of news is crucial. LLNewsBias provides the necessary groundwork for developing more robust and adaptable bias prediction models.

## Data Collection & Annotation

- **Sources:** The dataset is compiled from reputable sources such as Media Bias/Fact Check and Event Registry.
- **Annotation:** Headlines are carefully labeled with bias indicators, allowing researchers to explore political leanings across diverse contexts.
- **Coverage:** Focus on major events including Brexit, COVID-19, the 2020 U.S. election, and the Ukraine-Russia war.

## Key Features

- **Multilingual Coverage:** 17 languages to capture global perspectives.
- **Large-Scale Data:** Over 350,000 annotated news headlines.
- **Structured Organization:** Data is organized by event and year to facilitate focused research.
- **Support for Lifelong Learning:** Enables continuous model training and adaptation.

## Quick Start

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Swati17293/LLNewsBias.git
cd LLNewsBias
pip install -r requirements.txt
