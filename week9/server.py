from sqlalchemy import create_engine
from models import Website, Pages
from sqlalchemy.orm import Session
from connect import Base
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/search/')
def show_post():
    links = []
    keywords = request.args.get("keyword", "")
    keywords_list = keywords.split(" ")
    engine = create_engine("sqlite:///search.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    for keyword in keywords_list:
        keyword_query = "%" + keyword + "%"
        sites_by_title = session.query(Pages).filter(Pages.title.ilike(keyword_query))
        for site in sites_by_title:
            site_info = {"url": site.url, "title": site.title, "desc": site.desc}
            links.append(site_info)

        sites_by_desc = session.query(Pages).filter(Pages.desc.ilike(keyword_query))
        for site in sites_by_desc:
            site_info = {"url": site.url, "title": site.title, "desc": site.desc}
            if site_info not in links:
                links.append(site_info)

    return render_template("results.html", keywords=keywords, links=links)


if __name__ == "__main__":
    app.run(debug=True)  # When deploying without debug=True
