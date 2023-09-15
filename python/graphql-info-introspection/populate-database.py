from app import app, db, User, Post

with app.app_context():
    db.create_all()
    
    # Delete all existing records (Be careful with this in a real app!)
    User.query.delete()
    Post.query.delete()

    # Now add your new records
    john = User(username='johndoe', isAdmin=False)
    db.session.add(john)

    post = Post(title="Hello World", body="This is the first post of jhon")
    post.author = john
    db.session.add(post)

    jim = User(username='jimcarry', isAdmin=True)
    db.session.add(jim)

    post2 = Post(title="Woooow", body="I'm the maaaaask")
    post2.author = jim
    db.session.add(post2)

    post3 = Post(title="Second Post Jhon", body="This is the second post of jhon")
    post3.author = john
    db.session.add(post3)

    db.session.commit()