# Data Playground Build

**UI source [Data Play Dev](https://github.com/mr-robot0/dataplay-dev)**

> Data playground is simple UI developed in React.js and python's flask framework for playing with your data. You can perform different transformations, create interactive data visualizations and create and tune simple machine learning models.

> Data Play uses Flask as back end service for UI and React js for single page interactive web application experiance. For plotting i'm using plotly js as in-browser graph rendering engine. For data related operations such as cleaning, transforming and model training it uses 

## Usage

> Currently if you're using it on online mode it only supports `csv` files with maximum file size of 10 mb and one file at a time. If we can get enough funding and contribution we can extend these limits or You can download it and use it offline for your data science machine learning projects if you're absolute begginer or somewere between beginner and intermediat skill level without any limitations. 

#### Data

> On the home page you'lll find option to uplaod your file. Make sure it's csv. It will give you an overview of your data such as the head, decription and column info such column data type, it's categorical or not  , number of null values and number of unique values.

> This overview data will update with every cleaning operation you perform and every transformation you make.

### Transform

> Here you can preview your columns and apply different cleaning operations and transformations. For cleaning purposes we've only implemeted Imputer but we'll soon add custom transformations.

**Currently available transformations**

+ Numerical
   - MinMax Scaler
   - Normalizer
   - Standard Scaler

+  Categorical
    - Label Encoding
    - Dummy Variables / One Hot Encode

### Visualize

> In this section you can create interective visualization with different hues and sizes. Currently we're using plotly js for graph rendering. 

**Currently Available Visualizations**

1. Bar 
    - x : required / categorical
    - y : optional / will perforom average of y over x / numerical
    - hue : categorical

2. Line
    - x : required / numerical or categorical
    - y : optional / will plot x vs y line / numerical 
    - hue : not available / will add

3. Scatter
    - x : required / numerical or categorical
    - y : required / numercial or categorical
    - hue : categorical

4. Histogram
    - x : required / numerical
    - y : na
    - hue : not available / will add

5. Pie / Donut
    - x : required / categorical
    - y : na
    -hue : not available / will add
 
6. Box 
    - x : required / numerical
    - y : optional / will act as hue / categorical 
    - hue : use y

### Train 

> This section will allow you to create and tune simple machine learning models. Also this section provides auto validation for your trained model. It automatically plot errors and accuracy scores for your model on the bases of the data you provide. 

**Currently Available Algorithms**

1. Linear Regression
2. Logistic Regression