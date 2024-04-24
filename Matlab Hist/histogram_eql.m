% Loading an image
I = imread('dog.jpg');  

% Converting to grayscale if it is a color image
if size(I, 3) == 3
    I = rgb2gray(I);
end

% Applying histogram equalization
J = histeq(I);

% Displaying the original and equalized images
figure;
subplot(1, 2, 1);
imshow(I);
title('Original Image');

subplot(1, 2, 2);
imshow(J);
title('Equalized Image');

% Displaying histograms
figure;
subplot(1, 2, 1);
imhist(I);
title('Histogram of Original Image');

subplot(1, 2, 2);
imhist(J);
title('Histogram of Equalized Image');