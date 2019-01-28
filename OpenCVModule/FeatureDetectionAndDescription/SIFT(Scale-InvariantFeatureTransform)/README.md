# Goal
in this chapter,

+ We will learn about the concepts of SIFT algorithm
+ We will learn to find SIFT Keypoints and Descriptors.

# Thery
In last couple of chapters, we saw some corner detectors like Harris etc. They are rotation-invariant, which means, even if the image is rotated, we can find the same corners. It is obvious because corners remain corners in rotated image also. But what about scaling? A corner may not be a corner if the image is scaled. For example, check a simple image below. A corner in a small image within a small window is flat when it is zoomed in the same window. So Harris corner is not scale invariant.

