import pickle

# Load the model
with open("factory_ai_model.pkl", "rb") as file:
    model = pickle.load(file)

# Check the type of the loaded object
print("Loaded model type:", type(model))

# Check if it has a 'predict' method
if hasattr(model, "predict"):
    print("✅ Model is valid and has a predict method!")
else:
    print("❌ Model does NOT have a predict method! It might be a NumPy array or invalid object.")
