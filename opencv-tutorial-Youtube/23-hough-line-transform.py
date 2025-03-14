import numpy as np
import cv2

img = cv2.imread("../images/sudoku.jpg")
img = cv2.resize(img, (500, 500))
img = cv2.GaussianBlur(img, (5, 5), 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)
cv2.imshow("img2", edges)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y2), (x2, y2), (0, 255, 0), 1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
