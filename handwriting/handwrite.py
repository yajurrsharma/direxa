import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv("masti.csv")
input_cols = [f'Feature_{i}' for i in range(1, 16)] + ['Gender', 'Age']
output_cols = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
df = df[input_cols + output_cols]
df.dropna(inplace=True)

gender_map = {'Male': 0, 'Female': 1, 'Other': 2}
df['Gender'] = df['Gender'].map(gender_map)


X = df[input_cols]
y = df[output_cols]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print(X_scaled.shape)
print(y.shape)



X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y.values, test_size=0.2, random_state=42
)

print("Training data shape:", X_train.shape, y_train.shape)
print("Testing data shape:", X_test.shape, y_test.shape)


model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(5, activation='linear')  # 5 outputs for the 5 traits
])


model.compile(optimizer='adam', loss='mse', metrics=['mae'])



history = model.fit(
    X_train, y_train, 
    validation_split = 0.2,
    epochs=100, 
    batch_size = 16, 
    verbose=1
)

loss = model.evaluate(X_test, y_test)
print("Test Loss:", loss)
model.save("handwriting_personality_model.h5")

