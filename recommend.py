import pandas as pd

metadata = pd.read_csv('books.csv', low_memory=False)

metadata['average_rating'] = pd.to_numeric(metadata['average_rating'], errors='coerce')
metadata['ratings_count'] = pd.to_numeric(metadata['ratings_count'], errors='coerce')

metadata = metadata.dropna(subset=['average_rating', 'ratings_count'])

C = metadata['average_rating'].mean()

m = metadata['ratings_count'].quantile(0.90)

qualified = metadata[metadata['ratings_count'] >= m].copy()

def weighted_rating(x, m=m, C=C):
    v = x['ratings_count']
    R = x['average_rating']
    return (v / (v + m)) * R + (m / (v + m)) * C

qualified['score'] = qualified.apply(weighted_rating, axis=1)

top_books = qualified.sort_values('score', ascending=False).head(10)

print("Top 10 Book Recommendations:")
print(top_books[['title', 'authors', 'average_rating', 'ratings_count', 'score']])

while True:
    book_input = input("\n Enter a book title to view its details (or type 'exit' to quit): ").strip().lower()
    if book_input == 'exit':
        print("Goodbye!")
        break

    matched_books = metadata[metadata['title'].str.lower() == book_input]

    if not matched_books.empty:
        print("\n Book Found:")
        print(matched_books[['title', 'authors', 'average_rating', 'ratings_count']].to_string(index=False))
    else:
        print("Book doesn't exist. Please check the title and try again.")
        