# Guide of Can304 Group Project Code 

## 1. Files Introduction
This package consists of three python files
1. **can304.py**:Code of algorithms for encryption and decryption 
2. **main.py**:Starter of the program
3. **mainwindow.py**:User interface
## 2. How to run the code
### 2.1 Environment and Packages
Python3, sys, QApplication, QMainWindow, QtCore, QtGui, QtWidgets
### 2.2 Download Packages
In order to have a GUI, the necessary packages are required, the installation command are list as follow, you can download them in the terminal

​```
pip3 install PyQt5 -i https://pypi.douban.com/simple
​```

​```
pip3 install PyQt5-tools -i https://pypi.douban.com/simple
​```
### 2.3 Open main.py
Click run in the IDE, the GUI should be showed
### 2.4 Input plaintext and key on the left
If either plaintext or key is empty, encryption function will be invalid
### 2.5 Click Encryption to encrypt the plaintext
After clicking, the cipher will appear on the right
### 2.6 Click Decryption to decrypt the cipher
After clicking, the original plaintext will appear on the right
## 3. Some Testing Cases for Validation
| PlainText | Key    | Cipher           |
|:----------|:-------|:-----------------|
| HelloBob  | Crypto | O0Q3Q3W2O2X0W1R3 |
| CAN304    | xjtlu  | 921232400070     |
| CAN304    | ilove  | 03;181:0;030     |
| nihao     | shijie | f0d1l1g0a1       |


## 4. Note
The code was completed in a short time since the topic was chosen late. Therefore, the programme could have some bugs, we are happy to revise the code to fix bugs later.
  
Thanks for watching, Good Luck & Have Fun!