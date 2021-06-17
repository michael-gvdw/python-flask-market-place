from market import db

class UserModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=255), nullable=False, unique=True)
    email = db.Column(db.String(length=255), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=255), nullable=False)
    budget = db.Column(db.Float(), nullable=False, default=1000)
    products = db.relationship("ProductModel", backref='owned_user', lazy=True)

    def __repr__(self) -> str:
        return f"UserModel(id: {self.id}, username: {self.username}, email: {self.email}, budget: {self.budget})"


class ProductModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=255), nullable=False, unique=True)
    barcode = db.Column(db.String(length=255), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    user = db.Column(db.Integer(), db.ForeignKey("user_model.id"))

    def __repr__(self):
        return f"ProductModel(id: {self.id}, name: {self.name}, barcode: {self.barcode}, description: {self.description}, price: {self.price})"
