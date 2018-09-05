# starstr
This Python program was written to extract descent clusters from Y-STR data



## Prerequisites
* Python 2 (https://www.python.org/)
  * numpy



## Installation
```
git clone https://github.com/BoyanZhou/starstr
cd starstr
```
1. install
```
sudo python setup.py install
```
2. install it locally
```
python setup.py install --user
```



## Input
Input format is as follow:
```
ID1 Beijing    Han    study1    C3c-M48     C3   16  14  18  24  9   11  13  14  10  11  19  15  18  21  10    
ID2 Shanghai   Han    study1    Q1a3a       Q1a  13  13  17  24  10  14  13  13  11  12  19  15  16  22  11
ID3 Gansu      Hui    study2    R1a1a*-M17+ R1a1 17  12  17  25  11  11  13  14  9   10  20  16  15  23  13
```
The input file is tab-separated and each line shoud have the same number of columns. The first 6 columns can be used to store the sample info (e.g., 1-ID, 2-Location, 3-Population, 4-study number, 5-haplogroup detail, 6-haplogroup). These 6 columns can be empty, but TAB characters that separate tham are necesssay.




## Output



## Bug reporting
For any problem, please contact "boyanzhou1992@gmail.com".
