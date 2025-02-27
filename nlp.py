from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

courses = [
    "This course teaches about racer cars and vehicle mechanics.",
    "Learn about the physics and engineering of race cars.",
    "A deep dive into history and evolution of cars and automotive industry.",
]

model = KeyedVectors.load("word2vec-google-news-300.model", mmap='r')

def get_vector(description):
    words = description.lower().split()
    vectors = [model[word] for word in words if word in model]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

courses.append("This is about cars.")

course_vectors = np.array([get_vector(course) for course in courses])

similarity_matrix = cosine_similarity(course_vectors)

print(similarity_matrix)