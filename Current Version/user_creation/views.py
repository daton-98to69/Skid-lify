from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required,  current_user
from . import db
from .models import User, UserInfo
views = Blueprint('views', __name__)


@views.route('/', methods=["GET", "POST"])  # Decorator
@login_required
def home():
    # if request.method == 'POST':
    # note = request.form.get('note')

    # if len(note) < 1:
    #     flash('Note is too short!', catogery='error')
    # else:
    #     new_note = Note(data=note, user_id=current_user.id)
    #     db.session.add(new_note)
    #     db.session.commit()
    #     flash("Note added!", category='success')
    Current_user = UserInfo.query.filter_by(user_id=current_user.id).first()
    # print(Current_user)
    # clubs = Current_user.clubs
    return render_template("home.html", user=current_user, info=Current_user)  ## Small letter class calling works.



@views.route('/update_user_info', methods=['GET', 'POST'])
@login_required
def update_user_info():
    if request.method == 'POST':
        
        # If user info doesn't exist, create a new one
        new_user_info = UserInfo(
            subjects=request.form.get('subjects'),
            major=request.form.get('major'),
            quotes=request.form.get('quotes'),
            clubs=request.form.get('clubs'),
            profile_pic=request.form.get('profile_pic'),
            user_id=current_user.id
        )
        db.session.add(new_user_info)
        db.session.commit()
        flash("User info created!", category='success')
        
        return redirect(url_for('views.home', user=current_user))
    
    return render_template('update_user_info.html', user=current_user)
# def update_user_info():
#     if request.method == 'POST':
#         if current_user.user_info:

#         else:
#             current_user.user_info.append(UserInfo(
#                 subjects=request.form.get('subjects'),
#                 major=request.form.get('major'),
#                 quotes=request.form.get('quotes'),
#                 clubs=request.form.get('clubs'),
#                 profile_pic=request.form.get('profile_pic')
#             ))
#             db.session.commit()
#             flash("User info updated!", category='success')
#             return redirect(url_for('views.home', user=current_user))

#     return render_template('update_user_info.html', user=current_user)