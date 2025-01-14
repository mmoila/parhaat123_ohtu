from flask import render_template, request, redirect, flash
from services import reference_service as ref_service
from app import app


@app.route("/", methods=["GET", "POST"])
def main():
    # from ref.ref import Reference as ref
    if request.method =="GET":
        return render_template("main.html", refs=ref_service.get_references_normal())

    if request.method == "POST":
        field_values = request.form.to_dict()
        stripped_values = {key: field_values[key].strip() for key in field_values.keys()}
        
        if ref_service.create_book_reference(stripped_values):
            return render_template("main.html",
                                    message="Viite luotu onnistuneesti!",
                                    refs=ref_service.get_references_normal())
        return render_template("main.html",
                                message="Viitteen luonti ei onnistunut, kokeile toista avainta")

    # if request.method =="GET":
    #     return render_template("main.html", refs=ref.get_references_normal())

    # if request.method == "POST":
    #     keyword = request.form.get("keyword", "").strip()
    #     added_at = request.form.get("added_at", "").strip()
    #     author_surname = request.form.get("author_surname", "").strip()
    #     author_name = request.form.get("author_name", "").strip()
    #     title = request.form.get("title", "").strip()
    #     description = request.form.get("description", "").strip()
    #     url = request.form.get("url", "").strip()
    #     year = request.form.get("year", "").strip()
    #     reference_id = ref.create_reference('verkkosivu')

    #     if ref.create_website_reference(
    #         reference_id, keyword, added_at, author_surname,
    #         author_name, title, description, url, year):
    #         return render_template("main.html",
    #                                 message="Viite luotu onnistuneesti!",
    #                                 refs=ref.get_references_normal())
    return None
