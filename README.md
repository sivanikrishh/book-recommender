#  Top 10 Book Recommender

This is a mini project that recommends the **Top 10 highest-rated books** using a weighted rating formula. It also allows you to **search for any book** and see its details.

# Dataset

- The dataset used is `books.csv` 
- Required columns in the CSV:
  - `title` (book name)
  - `authors`
  - `average_rating`
  - `ratings_count`
 Can get book data from Kaggle or Goodreads exports.

# Logic Behind the Scoring

To avoid unfairness in rankings (like books with only 5 reviews being rated 5.0), we use a **weighted rating** formula:
score = (v / (v + m)) * R + (m / (v + m)) * C
Where:
- `R` = average rating of the book
- `v` = number of ratings the book received
- `m` = minimum number of ratings required to be listed (90th percentile)
- `C` = mean average rating of all books

📌 Notes
This project is inspired by a tutorial that built an IMDB movie recommender.

I adapted the logic to books instead of movies and tried to create it.

🌟 Future Improvements
>Add a web-based interface using Flask or Streamlit
>Show book covers using an API (like Google Books)

