from models.base import Base, Session, engine
from models.ads import Ad


def save_to_db(data):
    Base.metadata.create_all(engine)
    session = Session()
    for item in data:
        ad = Ad(title=item['title'],
                image=item['img-url'],
                date=item['date'],
                price=item['price'],
                currency=item['currency'],
                pagination=item['pagination']
                )
                
        session.add(ad)
    session.commit()
    session.close()