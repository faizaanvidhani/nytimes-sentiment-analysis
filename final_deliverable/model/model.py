import tensorflow as tf
import hyperparameters as hp
from preprocess import get_data
import os

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(hp.VOCAB_SIZE, hp.EMBEDDING_SIZE),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(hp.EMBEDDING_SIZE)),
        tf.keras.layers.Dense(hp.EMBEDDING_SIZE, activation='relu'),
        tf.keras.layers.Dense(hp.NUM_CLASSES, activation='softmax')
    ])
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
    model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model

def train_model():
    # Create the model
    model = create_model()
    model.summary()
    # Establish directory to save model to
    checkpoint_path = "saved_model/model4.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    # Get our training and test data
    train_padded, train_label_seq, test_padded, test_label_seq, _ = get_data()
    # Create a callback that saves the model's weights
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
        save_weights_only=True,
        verbose=1
    )
    # Train the model
    history = model.fit(train_padded, train_label_seq, epochs=hp.NUM_EPOCHS, validation_data=(test_padded, test_label_seq), 
        verbose=2, callbacks=[cp_callback]
    )