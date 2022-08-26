# Lab #1: Steganography

## <b>Objective</b>
During this activity, students will be able to:

Design and implement an image processing algorithm using bitwise operations in order to solve a steganographic problem.

Required Software
For this activity you will need to install the Pillow library and its type stub package. At the terminal type:

`pip install pillow types-Pillow`

Check the Pillow documentation for information on how to use this library.
[Pillow](https://pillow.readthedocs.io/en/stable/)

## Description

ste·ga·no·graph·y (noun)
The practice of concealing messages or information within other nonsecret text or data.
This activity must be developed in the pre-assigned teams of two.

We have the following processed PNG image file :

![image](https://user-images.githubusercontent.com/84719490/186955407-e20889ef-a811-4f36-a2e5-68da74054772.png)

There are three independent 1-bit images hidden in the least significant bit of every byte from each of the three color channels of the image.

Write a Python script called extract_hidden_images.py that:

Takes as a command line argument the name of an RGB mode PNG file. The program should print an error message and quit under the following circumstances:
The name of the file was not provided as a command line argument.
The provided file name doesn’t have a .png extension.
An exception is raised when trying to open the image file. It’s important to specify the reason as part of the error message.
The mode of the file is not RGB.
Extracts from the red, green, and blue channels the corresponding hidden 1-bit images placing the result in three 1-bit PNG images with the following suffixes after the original extensionless file-name :
- file-name_channel_1_red.png
- file-name_channel_2_green.png
- file-name_channel_3_blue.png

Example
Assuming the above image (scarlett.png) is stored in the same directory as your script you should be able to type at the terminal the following command:

`python extract_hidden_images.py scarlett.png`

The following three files should be created in the same directory where the `scarlett.png` file is located:

![image](https://user-images.githubusercontent.com/84719490/186956021-2faf5b7b-7cee-4d03-8174-205f531a3e16.png) `scarlett_channel_1_red.png`

![image](https://user-images.githubusercontent.com/84719490/186956099-c76cd335-b4d7-4279-96b0-0410ea86405d.png) `scarlett_channel_2_green.png`

![image](https://user-images.githubusercontent.com/84719490/186956157-7e191560-f66c-4139-8b9f-0a08bb3dfce4.png) `scarlett_channel_3_blue.png`


