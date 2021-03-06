# 4x4x3 3D convolution filter kernel, that can be used on 3 consecutive frames. This is a feature detection kernel.
FeatureKernel_4x4x3 = [[0.03, 0.03, 0.01166666666, 0.01166666666, 0.03, 0.03, 0.01166666666, 0.01166666666, 0.01166666666, 0.01166666666, 0.03, 0.03, 0.01166666666, 0.01166666666, 0.03, 0.03], [0.01166666666, 0.01166666666, 0.03, 0.03, 0.01166666666, 0.01166666666, 0.03, 0.03, 0.03, 0.03, 0.01166666666, 0.01166666666, 0.03, 0.03, 0.01166666666, 0.01166666666], [0.03, 0.03, 0.01166666666, 0.01166666666, 0.03, 0.03, 0.01166666666, 0.01166666666, 0.01166666666, 0.01166666666, 0.03, 0.03, 0.01166666666, 0.01166666666, 0.03, 0.03]]

# 4x4 Laplacian edge detection convolution filter kernel, that can be used on an image object to detect second order edges. A variant of this kernel can be used for edge enhancement
LaplacianEdgeKernel_4x4 = [-1.0, -1.0, -1.0, -1.0, -1.0, 3.0, 3.0, -1.0, -1.0, 3.0, 3.0, -1.0, -1.0, -1.0, -1.0, -1.0]

# 5x5 Gaussian smoothing kernel, can be used to smoothen the image - here standard deviation = 1
GaussianKernel_5x5 = [0.003765, 0.015019, 0.023792, 0.015019, 0.003765, 0.015019, 0.059912, 0.094907, 0.059912, 0.015019, 0.023792, 0.094907, 0.150342, 0.094907, 0.023792, 0.015019, 0.059912, 0.094907, 0.059912, 0.015019, 0.003765, 0.015019, 0.023792, 0.015019, 0.003765]

# 3x3 Sobel edge detection filters, can be used to detect edges in x and y direction
Sobel_x_3x3 = [1.0, 0.0, -1.0, 2.0, 0.0, -2.0, 1.0, 0.0, -1.0]
Sobel_y_3x3 = [1.0, 2.0, 1.0, 0.0, 0.0, 0.0, -1.0, -2.0, -1.0]
