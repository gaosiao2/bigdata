from flask import render_template, jsonify
from app.model.models import *
from . import index
from app import db
from sqlalchemy import func
from flask import Markup  # 导入 flask 中的 Markup 模块

@index.route("/monthly_comparison")
def _index():
    selectdata = db.session.query(Month_avg_quality.years, Month_avg_quality.months,
                                  Month_avg_quality.avg_quality).all()
    list_ = []
    for x in selectdata:
        data = {
            "dates": x.years + '-' + x.months,
            "avg_quality": x.avg_quality
        }
        list_.append(data)

    return render_template("index.html", month_avg_quality=list_)


@index.route("/time_count_top10")
def _index2():
    selectdata = db.session.query(Day_max_quality.time_point.label("time_point"), func.count(Day_max_quality.time_point).label("count")) \
        .group_by(Day_max_quality.time_point) \
        .order_by(func.count(Day_max_quality.time_point).desc()).limit(10).all()

    list_ = []
    for x in selectdata:
        data = {
            "time_point": str(x.time_point)[:-3],
            "count": x.count
        }
        list_.append(data)

    return render_template("index2.html", top10=list_)



def listparse(list1):
    list2 = []
    for list in list1:
        a = list / max(list1)
        list2.append(float('%.4f' % a))

    return list2

@index.route("/factors_affecting_quality")
def index3():
    selectdata = db.session.query(Year_avg_roaster.year.label("year"),Year_avg_roaster.avg_T.label("avg_T")
                                ,Year_avg_roaster.avg_H.label("avg_H"),Year_avg_roaster.avg_AH.label("avg_AH"),
                                Year_avg_quality.avg_quality.label("avg_quality")
                                  ).join(Year_avg_quality,Year_avg_roaster.year==Year_avg_quality.year)

    year=[]
    avg_T_list_ = []
    avg_H_list_ = []
    avg_AH_list_ = []
    avg_quality_list_ = []

    for x in selectdata:
        year.append(x.year)
        avg_T_list_.append(x.avg_T)
        avg_H_list_.append(x.avg_H)
        avg_AH_list_.append(x.avg_AH)
        avg_quality_list_.append(x.avg_quality)

    avg_T_list_=listparse(avg_T_list_)
    avg_H_list_=listparse(avg_H_list_)
    avg_AH_list_=listparse(avg_AH_list_)
    avg_quality_list_=listparse(avg_quality_list_)

    return render_template("index3.html", year=year,avg_T_list_=avg_T_list_,avg_H_list_=avg_H_list_,avg_AH_list_=avg_AH_list_,avg_quality_list_=avg_quality_list_)
