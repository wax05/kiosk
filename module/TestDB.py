from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Code(db.Model):
    """
    Sql Code Model
    - `CharSet` : utf8mb3_bin
    - `code` : VARCHAR(50)
    - `product_code` : VARCHAR(50)
    - `take` : VARCHAR(50)
    - `used` : TINYINT `0 == NotUsed`, `1 == Used`
    """
    __tablename__ = "code"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    code = db.Column(db.String(50,"utf8mb3_bin"))
    product_code = db.Column(db.String(50,"utf8mb3_bin"))
    take = db.Column(db.String(50,"utf8mb3_bin"))
    used = db.Column(db.Int(50,"utf8mb3_bin"))
    def __init__(self,code,product_code,take,used):
        self.code = code
        self.product_code = product_code
        self.take = take
        self.used = used
