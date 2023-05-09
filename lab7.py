import cv2

img = cv2.imread('image.jpg')
b, g, r = cv2.split(img)
original = cv2.merge((b, g, r))
combined_channel = cv2.hconcat([b, g, r])
cv2.imshow('Blue vs Green vs Red Channel', combined_channel)
g = g * 0
new_img = cv2.merge((b, g, r))
combined_img = cv2.hconcat([original, new_img])
cv2.imshow('Original vs. Modified Image', combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
