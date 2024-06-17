import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("C:\\Users\\my pc\\Desktop\\python_series\\codsoft_AI\\top 100 streamed_songs.csv")
print(df.head(3))

ss = StandardScaler()
features = ['tempo' , 'danceability' , 'energy' ]
songs_features = df[features]
scaled_features = ss.fit_transform(songs_features)
scaled_features_df = pd.DataFrame(scaled_features , columns=features)
# print(scaled_features_df.head(3))

similarity = cosine_similarity(scaled_features_df)
similarity_df = pd.DataFrame(similarity , index=df['name'] , columns=df['name'])
print(similarity_df.head(5))

def recommend_songs(name, similarity_df, df, num_recommendations=3):
    if name not in similarity_df.index:
        print(f"Song with ID '{name}' not found in the dataset.")
        return None
    
    song_index = similarity_df.index.get_loc(name)
    similarity_scores = list(similarity_df.iloc[song_index])
    similar_song_indices = np.argsort(similarity_scores)[::-1][1:num_recommendations+1]
    
    similar_songs = similarity_df.index[similar_song_indices].tolist()
    recommended_songs = df[df['name'].isin(similar_songs)]
    return recommended_songs


name = "Stay The Kid LAROI & Justin Bieber" 
recommended_songs = recommend_songs(name, similarity_df, df)
print(recommended_songs)