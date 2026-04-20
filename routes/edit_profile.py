from flask import render_template, Blueprint, render_template
from flask_login import login_required, current_user
from extensions import db
from models.user import UserTable
from models.profiles import Profile  # or wherever you placed itt
from flask import request, redirect, url_for
from flask_wtf import FlaskForm
from forms import EditProfileForm
from datetime import datetime

edit_profile_bp = Blueprint("edit_profile", __name__)


@edit_profile_bp.route("/edit/profile/", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm()
    profile = current_user.profile  # single source of truth

    if request.method == "GET":
        form.bio.data = profile.bio
        form.gender.data = profile.gender
        form.birthday.data = profile.birthday

    if request.method == "POST":
        profile.bio = request.form.get("bio")
        profile.gender = request.form.get("gender")

        birthday_str = request.form.get("birthday")
        if birthday_str:
            profile.birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()

        profile.image_url = request.form.get("image_url")

        db.session.commit()

        return redirect(url_for("profile.profile", user_id=current_user.id))

    return render_template(
        "edit_profile.html",
        profile=profile,
        form=form,
        user=current_user
    )