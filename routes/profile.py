from flask import render_template, Blueprint, render_template
from flask_login import login_required, current_user
from extensions import db
from models.user import UserTable
from models.profiles import Profile  # or wherever you placed itt

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile/<int:user_id>")
@login_required
def profile(user_id):
    user = UserTable.query.get_or_404(user_id)

    # ensure profile exists (safe fallback)
    if not user.profile:
        profile = Profile(user_id=user.id)
        db.session.add(profile)
        db.session.commit()

    return render_template("profile.html", user=user)
