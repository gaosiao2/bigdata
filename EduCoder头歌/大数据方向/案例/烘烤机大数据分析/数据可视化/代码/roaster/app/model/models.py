from app import db

class Month_avg_quality(db.Model):
    __tablename__ = "month_avg_quality"
    id=db.Column(db.Integer, primary_key=True) # 序号 主键
    years=db.Column(db.String(255))
    months=db.Column(db.String(255))
    avg_quality=db.Column(db.Integer)


class Day_max_quality(db.Model):
    __tablename__ = "day_max_quality"
    dates=db.Column(db.String(255), primary_key=True) # 序号 主键
    time_point=db.Column(db.String(255))
    max_quality=db.Column(db.Integer)


class Year_avg_roaster(db.Model):
    __tablename__ = "year_avg_roaster"
    year=db.Column(db.String(255), primary_key=True) # 序号 主键
    avg_T=db.Column(db.FLOAT)
    avg_H=db.Column(db.FLOAT)
    avg_AH = db.Column(db.FLOAT)

class Year_avg_quality(db.Model):
    __tablename__ = "year_avg_quality"
    year=db.Column(db.String(255), primary_key=True) # 序号 主键
    avg_quality=db.Column(db.FLOAT)



