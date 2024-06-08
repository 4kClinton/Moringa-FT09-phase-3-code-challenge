from database.setup import create_tables
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    try:
        
        create_tables()

        
        author1 = Author(name="John Doe")
        print(f"Author ID: {author1.id}, Name: {author1.name}")

        
        magazine1 = Magazine(name="Tech Weekly", category="Technology")
        print(f"Magazine ID: {magazine1.id}, Name: {magazine1.name}, Category: {magazine1.category}")

        
        article1 = Article(author=author1, magazine=magazine1, title="AI in 2024", content="Content about AI advancements in 2024")
        print(f"Article ID: {article1.id}, Title: {article1.title}, Author: {article1.author.name}, Magazine: {article1.magazine.name}")
        print("Author's Articles:", author1.articles())
        print("Author's Magazines:", author1.magazines())
        print("Magazine's Articles:", magazine1.articles())
        print("Magazine's Contributors:", magazine1.contributors())
        print("Magazine's Article Titles:", magazine1.article_titles())
        print("Magazine's Contributing Authors:", magazine1.contributing_authors())

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "_main_":
    main()