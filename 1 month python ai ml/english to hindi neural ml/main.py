## Import Necesary Libraries
import pandas as pd
import tensorflow as tf
import keras
from keras import layers
import numpy as np
from sklearn.model_selection import train_test_split
from keras.layers import LSTM, Dense, Input, Embedding
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string

import warnings

warnings.filterwarnings("ignore")

data = pd.read_csv("/content/Hindi_English_Truncated_Corpus.csv", engine="python")
data.head(3)
# counting sources
data["source"].value_counts()
sns.countplot(x="source", data=data)
plt.show()
print("Total data: ", data.shape[0])
# selcting data with source ted
data = data[data.source == "ted"]
data.shape
# checking null values
data.isna().sum()
# checking duplicated data
isDuplicated = data.duplicated().any()
if isDuplicated:
    total_duplicates = data.duplicated().sum()
    print("Total duplicate rows are: ", total_duplicates)
    data.drop_duplicates(inplace=True)
## sampling rows randomly
data = data.sample(n=2000, random_state=31)
data.shape
## Text preprocessing
## changing uppercase to lowercase
data["english_sentence"] = data["english_sentence"].apply(lambda x: x.lower())
data["hindi_sentence"] = data["hindi_sentence"].apply(lambda x: x.lower())

# Remove quotes
data["english_sentence"] = data["english_sentence"].apply(lambda x: re.sub("'", "", x))
data["hindi_sentence"] = data["hindi_sentence"].apply(lambda x: re.sub("'", "", x))

to_exclude = set(string.punctuation)  # Set of all special characters
print("punctuations to exclude:: ", to_exclude)
# Remove all the special characters
data["english_sentence"] = data["english_sentence"].apply(
    lambda x: "".join(ch for ch in x if ch not in to_exclude)
)
data["hindi_sentence"] = data["hindi_sentence"].apply(
    lambda x: "".join(ch for ch in x if ch not in to_exclude)
)
from string import digits

# Remove all numbers from text
remove_digits = str.maketrans("", "", digits)

data["english_sentence"] = data["english_sentence"].apply(
    lambda x: x.translate(remove_digits)
)
data["hindi_sentence"] = data["hindi_sentence"].apply(
    lambda x: x.translate(remove_digits)
)

data["hindi_sentence"] = data["hindi_sentence"].apply(
    lambda x: re.sub("[२३०८१५७९४६]", "", x)
)

# Remove extra spaces
data["english_sentence"] = data["english_sentence"].apply(lambda x: x.strip())
data["hindi_sentence"] = data["hindi_sentence"].apply(lambda x: x.strip())
data["english_sentence"] = data["english_sentence"].apply(
    lambda x: re.sub(" +", " ", x)
)
data["hindi_sentence"] = data["hindi_sentence"].apply(lambda x: re.sub(" +", " ", x))
## adding start and end token to the target sentence
data["hindi_sentence"] = data["hindi_sentence"].apply(lambda x: "START_ " + x + " _END")
## counting length of english and hindi sentence
data["english_length"] = data["english_sentence"].apply(lambda x: len(x.split(" ")))
data["hindi_length"] = data["hindi_sentence"].apply(lambda x: len(x.split(" ")))

data.head()
print("Maximum length of English Sentence: ", max(data["english_length"]))
print("Maximum length of Hindi Sentence: ", max(data["hindi_length"]))
### Get English and Hindi Vocabulary
all_eng_words = set()
for eng in data["english_sentence"]:
    for word in eng.split():
        if word not in all_eng_words:
            all_eng_words.add(word)

all_hindi_words = set()
for hin in data["hindi_sentence"]:
    for word in hin.split():
        if word not in all_hindi_words:
            all_hindi_words.add(word)


print("toral english words: ", len(all_eng_words))
print("total hind words: ", len(all_hindi_words))
## using only sentence with length less than 20
mask1 = data["english_length"] < 21
mask2 = data["hindi_length"] < 21
data = data[mask1 & mask2]
data.shape
print("maximum length of Hindi Sentence ", max(data["hindi_length"]))
print("maximum length of English Sentence ", max(data["english_length"]))
input_words = sorted(list(all_eng_words))
target_words = sorted(list(all_hindi_words))
num_encoder_tokens = len(all_eng_words)
num_decoder_tokens = len(all_hindi_words)

num_encoder_tokens, num_decoder_tokens
num_decoder_tokens += 1  # for zero padding

input_token_index = dict([(word, i + 1) for i, word in enumerate(input_words)])
target_token_index = dict([(word, i + 1) for i, word in enumerate(target_words)])
print("Token for 'a' is: ", input_token_index["a"])
input_token_index = dict([(word, i + 1) for i, word in enumerate(input_words)])
target_token_index = dict([(word, i + 1) for i, word in enumerate(target_words)])
print("Token for 'a' is: ", input_token_index["a"])
# splitting data
X_, y_ = data["english_sentence"], data["hindi_sentence"]
X_train, X_test, y_train, y_test = train_test_split(
    X_, y_, test_size=0.2, random_state=42
)
print("Total number of training data: ", X_train.shape[0])
print("Toral number of testing data: ", X_test.shape[0])
latent_dim = 300
# Encoder
encoder_inputs = Input(shape=(None,))
enc_emb = Embedding(num_encoder_tokens + 1, latent_dim, mask_zero=True)(encoder_inputs)
encoder_lstm = LSTM(latent_dim, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(enc_emb)
# We discard `encoder_outputs` and only keep the states.
encoder_states = [state_h, state_c]


# Set up the decoder, using `encoder_states` as initial state.
decoder_inputs = Input(shape=(None,))
dec_emb_layer = Embedding(num_decoder_tokens, latent_dim, mask_zero=True)
dec_emb = dec_emb_layer(decoder_inputs)
# We set up our decoder to return full output sequences,
# and to return internal states as well. We don't use the
# return states in the training model, but we will use them in inference.
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(dec_emb, initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation="softmax")
decoder_outputs = decoder_dense(decoder_outputs)

# Define the model that will turn
# `encoder_input_data` & `decoder_input_data` into `decoder_target_data`
model = tf.keras.Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.summary()
model.compile(
    optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
)
max_length_src = 20
max_length_tar = 20


def generate_batch(X=X_train, y=y_train, batch_size=128):
    """Generate a batch of data"""
    while True:
        for j in range(0, len(X), batch_size):
            encoder_input_data = np.zeros((batch_size, max_length_src), dtype="float32")
            decoder_input_data = np.zeros((batch_size, max_length_tar), dtype="float32")
            decoder_target_data = np.zeros(
                (batch_size, max_length_tar, num_decoder_tokens), dtype="float32"
            )
            for i, (input_text, target_text) in enumerate(
                zip(X[j : j + batch_size], y[j : j + batch_size])
            ):
                for t, word in enumerate(input_text.split()):
                    encoder_input_data[i, t] = input_token_index[
                        word
                    ]  # encoder input seq
                for t, word in enumerate(target_text.split()):
                    if t < len(target_text.split()) - 1:
                        decoder_input_data[i, t] = target_token_index[
                            word
                        ]  # decoder input seq
                    if t > 0:
                        # decoder target sequence (one hot encoded)
                        # does not include the START_ token
                        # Offset by one timestep
                        decoder_target_data[i, t - 1, target_token_index[word]] = 1.0
            yield ((encoder_input_data, decoder_input_data), decoder_target_data)


train_samples = len(X_train)
val_samples = len(X_test)
batch_size = 128
epochs = 1
model.fit(
    generate_batch(X_train, y_train, batch_size=batch_size),
    steps_per_epoch=train_samples // batch_size,
    epochs=epochs,
    validation_data=generate_batch(X_test, y_test, batch_size=batch_size),
    validation_steps=val_samples // batch_size,
)
# Encode the input sequence to get the "thought vectors"
encoder_model = tf.keras.Model(encoder_inputs, encoder_states)

# Decoder setup
# Below tensors will hold the states of the previous time step
decoder_state_input_h = Input(shape=(latent_dim,))
decoder_state_input_c = Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]

dec_emb2 = dec_emb_layer(decoder_inputs)  # Get the embeddings of the decoder sequence

# To predict the next word in the sequence, set the initial states to the states from the previous time step
decoder_outputs2, state_h2, state_c2 = decoder_lstm(
    dec_emb2, initial_state=decoder_states_inputs
)
decoder_states2 = [state_h2, state_c2]
decoder_outputs2 = decoder_dense(
    decoder_outputs2
)  # A dense softmax layer to generate prob dist. over the target vocabulary

# Final decoder model
decoder_model = tf.keras.Model(
    [decoder_inputs] + decoder_states_inputs, [decoder_outputs2] + decoder_states2
)


def decode_sequence(input_seq):
    # Encode the input as state vectors.
    states_value = encoder_model.predict(input_seq)
    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1))
    # Populate the first character of target sequence with the start character.
    target_seq[0, 0] = target_token_index["START_"]

    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    stop_condition = False
    decoded_sentence = ""
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = reverse_target_word_index[sampled_token_index]
        decoded_sentence += " " + sampled_char

        # Exit condition: either hit max length
        # or find stop character.
        if sampled_char == "_END" or len(decoded_sentence) > 50:
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index

        # Update states
        states_value = [h, c]

    return decoded_sentence


train_gen = generate_batch(X_train, y_train, batch_size=1)
k = -1

k += 1
(input_seq, actual_output), _ = next(train_gen)
decoded_sentence = decode_sequence(input_seq)
print("Input English sentence:", X_train[k : k + 1].values[0])
print("Actual Hindi Translation:", y_train[k : k + 1].values[0][6:-4])
print("Predicted Hindi Translation:", decoded_sentence[:-4])
k = k + 1
(input_seq, actual_output), _ = next(train_gen)
decoded_sentence = decode_sequence(input_seq)
print("Input English sentence:", X_train[k : k + 1].values[0])
print("Actual Hindi Translation:", y_train[k : k + 1].values[0][6:-4])
print("Predicted Hindi Translation:", decoded_sentence[:-4])
k = k + 1
(input_seq, actual_output), _ = next(train_gen)
decoded_sentence = decode_sequence(input_seq)
print("Input English sentence:", X_train[k : k + 1].values[0])
print("Actual Hindi Translation:", y_train[k : k + 1].values[0][6:-4])
print("Predicted Hindi Translation:", decoded_sentence[:-4])
k = k + 1
(input_seq, actual_output), _ = next(train_gen)
decoded_sentence = decode_sequence(input_seq)
print("Input English sentence:", X_train[k : k + 1].values[0])
print("Actual Hindi Translation:", y_train[k : k + 1].values[0][6:-4])
print("Predicted Hindi Translation:", decoded_sentence[:-4])
k = k + 1
(input_seq, actual_output), _ = next(train_gen)
decoded_sentence = decode_sequence(input_seq)
print("Input English sentence:", X_train[k : k + 1].values[0])
print("Actual Hindi Translation:", y_train[k : k + 1].values[0][6:-4])
print("Predicted Hindi Translation:", decoded_sentence[:-4])
k = k + 1
(input_seq, actual_output), _ = next(train_gen)
decoded_sentence = decode_sequence(input_seq)
print("Input English sentence:", X_train[k : k + 1].values[0])
print("Actual Hindi Translation:", y_train[k : k + 1].values[0][6:-4])
print("Predicted Hindi Translation:", decoded_sentence[:-4])
