import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Define text properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
font_color = (255, 255, 255)  # White color

# Add names to the image using putText()
cv2.putText(img, "Mercury", (50, 200), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Venus", (200, 300), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Earth", (350, 400), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Mars", (500, 500), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Jupiter", (650, 600), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Saturn", (800, 700), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Uranus", (950, 800), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Neptune", (1100, 900), font, font_scale, font_color, font_thickness)

# Display the image
cv2.imshow("Solar System with Names", img)
cv2.waitKey(0)

# Save the modified image
cv2.imwrite("Solar_system_with_name.jpg", img)

# Close all windows
cv2.destroyAllWindows()
