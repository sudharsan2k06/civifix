from model import predict_issue

# Put ANY image path here (road, street, garbage, etc.)
image_path = r"C:\Users\sudha\OneDrive\Desktop\civic-issuse-reporter\uploads\36.jpg"
result = predict_issue(image_path)
print("Prediction:", result)
