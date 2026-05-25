from flask import render_template, Blueprint, render_template
from flask_login import login_required, current_user
from extensions import db
from models.profile_change import ProfileChangeLog
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
    profile = current_user.profile

    if request.method == "GET":
        form.bio.data = profile.bio
        form.gender.data = profile.gender
        form.birthday.data = profile.birthday
        if hasattr(form, "image_url"):
            form.image_url.data = profile.image_url

        return render_template(
            "edit_profile.html",
            form=form,
            profile=profile,
            user=current_user
        )

    if request.method == "POST":

        for field_name, field in form._fields.items():

            if field_name in ["csrf_token", "submit"]:
                continue

            if not hasattr(profile, field_name):
                continue

            old_value = getattr(profile, field_name)
            new_value = field.data

            if field_name == "birthday" and new_value:
                try:
                    new_value = datetime.strptime(str(new_value), "%Y-%m-%d").date()
                except ValueError:
                    new_value = None

            if old_value != new_value:
                setattr(profile, field_name, new_value)

                db.session.add(ProfileChangeLog(
                    user_id=current_user.id,
                    field=field_name,
                    old_value=str(old_value),
                    new_value=str(new_value)
                ))

        db.session.commit()
        return redirect(url_for("profile.profile", user_id=current_user.id))

    return render_template(
        "edit_profile.html",
        profile=profile,
        form=form,
        user=current_user
    )