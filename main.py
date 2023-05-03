from flask import Flask, render_template, request, redirect, send_file
from extractors.weworkremotely import extract_weworkremotely_jobs
from file import save_to_file

app = Flask("Job Scraper")

@app.route("/")
def home():
    return render_template("home.html")

data_base = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    keyword = keyword.replace(" ", "_")
    if keyword in data_base:
        jobs = data_base[keyword]
    else:
        keyword = keyword.replace("_", " ")
        jobs = extract_weworkremotely_jobs(keyword)
        keyword = keyword.replace(" ", "_")
        data_base[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword not in data_base:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, data_base[keyword])
    return send_file(f"{keyword}_jobs_data.csv", as_attachment=True)

if __name__ == "__main__":
    app.run("0.0.0.0")