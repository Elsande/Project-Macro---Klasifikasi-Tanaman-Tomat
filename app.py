import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import custom_object_scope, register_keras_serializable
import tensorflow_hub as hub
import streamlit as st
import numpy as np

# Function to predict image
def predict_image(model, img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    return predicted_class_index

custom_objects = {'KerasLayer': hub.KerasLayer}

# Load the model
with custom_object_scope(custom_objects):
    model = tf.keras.models.load_model('./model/macro_project.h5')

# Streamlit app
st.title("Plant Disease Prediction App")
image_path = st.file_uploader("Choose an Image:")

if image_path is not None:
    st.image(image_path, width=4, use_column_width=True)

# Predict button
if st.button("Predict"):
    st.write("Prediction Results")
    result = predict_image(model, image_path)

    # Class mapping
    class_mapping = ['Early_blight', 'Healthy', 'Late_blight', 'Leaf Miner', 'Magnesium Deficiency', 'Nitrogen Deficiency', 'Pottassium Deficiency', 'Spotted Wilt Virus']

    # Save the prediction result to a variable
    prediction = class_mapping[result]

    # Display the prediction result
    st.success("Model is Predicting it's a {}".format(prediction))

        # Display more details about the prediction
    disease_info = {
        "Early_blight": "The plant is likely infected with Early Blight, which is a common fungal disease that affects tomatoes, potatoes, and other members of the Solanaceae family. It is characterized by the appearance of concentric rings of dead tissue on the leaves, stems, and fruits. To manage this disease, it is recommended to remove and destroy infected plants, rotate crops, and use resistant varieties.",
        "Healthy": "The plant appears to be healthy. Keep up the good work!",
        "Late_blight": "The plant is likely infected with Late Blight, which is a serious disease that affects potatoes, tomatoes, and other members of the Solanaceae family. It is caused by a fungus-like organism and is characterized by the appearance of large, water-soaked lesions on the leaves, stems, and fruits. To manage this disease, it is recommended to remove and destroy infected plants, rotate crops, and use resistant varieties.",
        "Leaf Miner": "The plant is likely infested with Leaf Miners, which are small flies that lay their eggs on the leaves of plants. The larvae then feed on the leaf tissue, creating winding tunnels that are visible on the leaf surface. To manage this pest, it is recommended to remove and destroy infested leaves, use insecticidal soap or neem oil, and encourage beneficial insects that prey on Leaf Miners.",
        "Magnesium Deficiency": "The plant is likely suffering from Magnesium Deficiency, which is a common nutrient disorder that affects many types of plants. It is characterized by the appearance of interveinal chlorosis, or yellowing between the veins, on the older leaves. To manage this disorder, it is recommended to apply a magnesium-containing fertilizer, such as Epsom salts, and maintain proper soil pH.",
        "Nitrogen Deficiency": "The plant is likely suffering from Nitrogen Deficiency, which is a common nutrient disorder that affects many types of plants. It is characterized by the appearance of chlorosis, or yellowing, on the older leaves. To manage this disorder, it is recommended to apply a nitrogen-containing fertilizer and maintain proper soil pH.",
        "Pottassium Deficiency": "The plant is likely suffering from Potassium Deficiency, which is a common nutrient disorder that affects many types of plants. It is characterized by the appearance of necrosis, or browning, on the leaf margins and tips. To manage this disorder, it is recommended to apply a potassium-containing fertilizer and maintain proper soil pH.",
        "Spotted Wilt Virus": "The plant is likely infected with Spotted Wilt Virus, which is a viral disease that affects many types of plants. It is transmitted by thrips and is characterized by the appearance of small, dark spots on the leaves and fruits. To manage this disease, it is recommended to remove and destroy infected plants, control thrips, and use resistant varieties."
    }

    st.write(disease_info[prediction])