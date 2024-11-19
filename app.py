from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from database import JOBS
from create_db import my_cursor,mydb, load_jobs_from_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:System@12345/@localhost/job_details'



@app.route("/")
def hello_world():
    jobs=load_jobs_from_db()
    return render_template("home.html",
                           jobs=jobs)


'''@app.route("/job/<int:job_id>")
def job_details(job_id):
    # Find the job by ID
    job = next((job for job in JOBS if job['id'] == job_id), None)

    if not job:
        return "Job not found", 404

    # Render a template with job details
    return render_template("jobdetails.html", job=job)

@app.route("/job/<int:job_id>/apply", methods=['POST'])
def apply_job(job_id):
    data=request.form
    job=job_details(job_id)
    return render_template('application_submitted.html',
                           application=data,
                           job=job)'''

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
