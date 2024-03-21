from models import db, Joke
from jokes import jokes_seed

def seed_db():
    if Joke.query.first() is None:
        for joke in jokes_seed:
            new_joke = Joke(text=joke["text"], level=joke["level"], lang=joke["lang"])
            db.session.add(new_joke)

        db.session.commit()
        print('Database seeded!')
    else:
        print('Database already has jokes, skipping seed.')