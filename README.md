# Fire Weather Index Prediction App

This Flask web application predicts the Fire Weather Index (FWI) based on user-provided weather data. It utilizes a Ridge regression model to make predictions using inputs such as temperature, relative humidity, wind speed, and other relevant features.

## Project Overview

### Algerian Forest Fires Data Analysis

The dataset used in this project is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset). It includes observations of forest fires in two regions of Algeria: Bejaia and Sidi Bel-Abbes. The dataset spans from June 2012 to September 2012. 

The goal of this project is to analyze whether specific weather features can effectively predict the occurrence of forest fires in these regions by employing various classification algorithms.

### Data Collection and Understanding

- **Weather Data Observations**:
  - **Temp**: Maximum noon temperature in Celsius (22 to 42°C)
  - **RH**: Relative Humidity in % (21 to 90%)
  - **Ws**: Wind speed in km/h (6 to 29 km/h)
  - **Rain**: Total daily rain in mm (0 to 16.8 mm)

- **FWI Components**:
  - **Fine Fuel Moisture Code (FFMC)**: 28.6 to 92.5
  - **Duff Moisture Code (DMC)**: 1.1 to 65.9
  - **Initial Spread Index (ISI)**: 0 to 18.5
  - **Fire Weather Index (FWI)**: 0 to 31.1
  - **Classes**: Two classes indicating the regions:
    - **0**: Bejaia region
    - **1**: Sidi Bel-Abbes region

## Features

- User-friendly interface for inputting weather parameters.
- Predicts the Fire Weather Index based on user input.
- Built with Flask, using a pre-trained Ridge regression model and data scaling.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For machine learning model implementation.
- **Pickle**: For loading pre-trained machine learning models.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps to Run the Application

1. **Clone the repository:**

   ```bash
   git clone https://github.com/CodeHarshh/TestForestFire.git
   cd TestForestFire





