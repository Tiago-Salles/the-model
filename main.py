import math

# Example of a simple word-to-vector mapping (training phase)
word_to_vector = {
    "dog": [0.1, 0.3, 0.5],
    "cat": [0.2, 0.4, 0.6],
    "chase": [0.3, 0.2, 0.1],
    "play": [0.4, 0.4, 0.4],
    "ball": [0.5, 0.5, 0.7],
    "toy": [0.6, 0.6, 0.8]
}

# Tokenization: Convert the message into words and find their vector representations
def tokenize(message):
    tokens = message.lower().split()  # Simple split by space and lowercase
    return [word_to_vector.get(word) for word in tokens if word in word_to_vector]

# Calculate cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    # Dot product
    dot_product = sum([a * b for a, b in zip(vec1, vec2)])
    # Magnitudes (norms)
    magnitude1 = math.sqrt(sum([a * a for a in vec1]))
    magnitude2 = math.sqrt(sum([b * b for b in vec2]))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # Avoid division by zero
    return dot_product / (magnitude1 * magnitude2)

# Compare the tokenized message with trained content
def find_most_relevant_answer(message):
    tokens = tokenize(message)
    if not tokens:
        return "No relevant tokens found."
    
    best_match = None
    best_similarity = -1
    
    # Predefined "trained" content (simple examples)
    trained_content = {
        "dog plays": ["dog", "play", "ball"],
        "cat plays": ["cat", "play", "toy"]
    }
    
    for key, value in trained_content.items():
        key_tokens = tokenize(key)
        if not key_tokens:
            continue
        
        # Compute similarity: average cosine similarity between token vectors
        similarity = 0
        for token_vector in tokens:
            for key_vector in key_tokens:
                similarity += cosine_similarity(token_vector, key_vector)
        
        similarity /= (len(tokens) * len(key_tokens))  # Average similarity
        
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = key
    
    return f"Most relevant answer: {best_match}" if best_match else "No relevant match found."

# Example input
message = "toy"
response = find_most_relevant_answer(message)
print(response)